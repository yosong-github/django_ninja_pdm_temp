from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


# 模拟国际化，后面添加多语言支持
def _(*args, **kwargs):
    return args[0] if args else ""


class RequestModel(BaseModel):
    class Config(ConfigDict):
        validate_by_name = True  # 允许 user_id / userId


class ResponseModel(BaseModel):
    class Config(ConfigDict):
        validate_by_name = True  # 允许 user_id / userId

    # 检查message字段，后期可以添加多语言支持
    @field_validator("message", check_fields=False)
    def translations_message(cls, message):
        return message


class ResponseStatus(int, Enum):
    SUCCESS = 200
    ERROR = 500
    UNKNOWN_REQUEST = 400
    # 无权限
    PERMISSION_DENIED = 403
    # 未找到
    NOT_FOUND = 404


class BoolResponse(ResponseModel):
    code: ResponseStatus = ResponseStatus.SUCCESS
    message: str = _("操作成功")


class StrDataResponse(ResponseModel):
    code: ResponseStatus = ResponseStatus.SUCCESS
    message: str = _("操作成功")
    data: str = Field(None)


class UploadFileResponse(BoolResponse):
    data: UUID = Field(title="文件ID")


class DataDictResponse(ResponseModel):
    code: ResponseStatus = ResponseStatus.SUCCESS
    message: str = _("操作成功")
    data: dict = Field(None)


class DataListResponse(ResponseModel):
    code: ResponseStatus = ResponseStatus.SUCCESS
    message: str = _("操作成功")
    data: list = Field(None)


class PageList(BaseModel):
    page: int
    page_size: int
    total_pages: int = 1
    amount: int = 0
    data: list = Field(None)


class PageListResponse(ResponseModel):
    code: ResponseStatus = ResponseStatus.SUCCESS
    message: str = _("操作成功")
    data: PageList = Field(None)
