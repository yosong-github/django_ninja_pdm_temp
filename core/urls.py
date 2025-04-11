"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import logging

from django.urls import path
from ninja import NinjaAPI
from ninja.errors import AuthenticationError, ValidationError
from ninja.security import HttpBearer

from apps.user.apis import router as user_router
from apps.user.auth import verify_token
from utils.api.error import ApplicationError, UserLoginFailed


class GlobalAuth(HttpBearer):
    # 定义登录
    def authenticate(self, request, token):
        user_id = verify_token(token)
        if user_id:
            return token


api = NinjaAPI(csrf=False, auth=GlobalAuth())
api.add_router("user", user_router, tags=["用户"])


# 自定义服务器错误（应用程序未处理的任何其他异常。 默认行为）
@api.exception_handler(Exception)
def validation_errors(request, exc):
    logging.error(f"服务出错:{str(exc)}", exc_info=True)
    return api.create_response(
        request,
        {"code": 500, "message": "服务器发生错误,请稍后再试或联系相关人员"},
        status=200,
    )


# 自定义认证错误（当请求未通过认证时抛出）
@api.exception_handler(AuthenticationError)
def validation_errors_auth(request, exc):
    return api.create_response(
        request,
        {"code": UserLoginFailed.code, "message": UserLoginFailed.message},
        status=200,
    )


# 自定义验证错误（当请求数据未通过验证时抛出）
@api.exception_handler(ValidationError)
def validation_errors_validation(request, exc):
    return api.create_response(
        request,
        {"code": 422, "message": "参数错误：" + str(exc)},
        status=200,
    )


# 自定义自定义错误（逻辑错误，有开发者抛出的错误）
@api.exception_handler(ApplicationError)
def validation_errors_app(request, exc: ApplicationError):
    return api.create_response(
        request,
        {"code": exc.code, "message": exc.message},
        status=200,
    )


urlpatterns = [path("api/", api.urls)]
