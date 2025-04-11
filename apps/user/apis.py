from django.core.cache import cache
from django.forms.models import model_to_dict
from django.http import HttpRequest
from ninja import Router
from pydantic import BaseModel

from utils.api.error import UserAuthFailed, UserLoginFailed, UserTokenWasExpired
from utils.api.request import get_authorization_scheme_token
from utils.api.response import DataDictResponse, PageListResponse
from utils.pagination import paginate

from .auth import generate_tokens, refresh_access_token, verify_token
from .models import SysUser

router = Router()


class LoginRequest(BaseModel):
    username: str
    password: str

    # 自定义请求体的示例值
    class Config:
        json_schema_extra = {"example": {"username": "yosong", "password": "158598"}}


@router.post("login", summary="用户登录", auth=None)
def login(request, login_data: LoginRequest):
    user = SysUser.objects.filter(username=login_data.username, password=login_data.password).first()
    if not user:
        raise UserAuthFailed()
    # 通过用户ID生成token
    access_token, refresh_token = generate_tokens(user.id)
    cache.set(f"refresh_token_{user.id}", refresh_token, timeout=None)
    cache.set(f"access_token_{user.id}", access_token, timeout=None)

    return DataDictResponse(
        data={
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
    )


@router.get("refresh_token", summary="刷新用户token")
def app_refresh_token(request: HttpRequest, refresh_token: str):
    authorization: str = request.headers.get("Authorization")
    if not authorization:
        raise UserLoginFailed

    token, scheme = get_authorization_scheme_token(request)
    user = verify_token(token)
    user_orm = SysUser.objects.get(id=user["user_id"])
    user_cache = cache.get(f"refresh_token_{user_orm.id}")

    if user_orm and user_cache == refresh_token:
        access_token, refresh_token = refresh_access_token(refresh_token)
        cache.set(f"refresh_token_{user_orm.id}", refresh_token, timeout=None)
        cache.set(f"access_token_{user_orm.id}", access_token, timeout=None)
        return DataDictResponse(
            data={
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        )
    raise UserTokenWasExpired


@router.get("/list", response=PageListResponse)
def list_users(request: HttpRequest, page: int = 1, page_size: int = 10, name: str = ""):
    return paginate(page, page_size, SysUser.objects.filter(username__contains=name))


class User(BaseModel):
    username: str
    password: str
    user_type: int


@router.post("add", summary="添加用户", description="添加一条用户", response=DataDictResponse)
def add_user(request, user_data: User):
    user = SysUser.objects.create(**dict(user_data))
    print(user)
    return DataDictResponse(data=model_to_dict(user))
