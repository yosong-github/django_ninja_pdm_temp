from django.forms.models import model_to_dict
from ninja import Router
from pydantic import BaseModel

from utils.api.error import UserAuthFailed
from utils.api.response import DataDictResponse, DataListResponse

from .auth import generate_tokens
from .models import SysUser

router = Router()


class LoginRequest(BaseModel):
    username: str
    password: str

    # 自定义请求体的示例值
    class Config:
        json_schema_extra = {"example": {"username": "yosong", "password": "158598"}}



@router.post(
    "login",
    summary="用户登录",
    description="用户登录",
    auth=None
)
def login(request, login_data: LoginRequest):
    user = SysUser.objects.filter(username=login_data.username, password=login_data.password).first()
    if not user:
        raise UserAuthFailed()
    # 通过用户ID生成token
    access_token, refresh_token = generate_tokens(user.id)
    print(access_token, refresh_token)
    return DataDictResponse(
        data={
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
    )


@router.get(
    "list",
    summary="获取用户列表",
    description="返回所有用户的列表",
    response=DataListResponse,
)
def get_users(request):
    user_list = SysUser.objects.all()
    data = [model_to_dict(user) for user in user_list]
    return DataListResponse(data=data)


class User(BaseModel):
    username: str
    password: str
    user_type: int


@router.post("add", summary="添加用户", description="添加一条用户", response=DataDictResponse)
def add_user(request, user_data: User):
    user = SysUser.objects.create(**dict(user_data))
    print(user)
    return DataDictResponse(data=model_to_dict(user))
