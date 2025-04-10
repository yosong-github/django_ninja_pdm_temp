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
from django.urls import path
from ninja import NinjaAPI
from ninja.security import HttpBearer

from apps.user.apis import router as user_router
from apps.user.auth import verify_token


class GlobalAuth(HttpBearer):
    # 定义登录
    def authenticate(self, request, token):
        print(token)
        print()
        user_id = verify_token(token)
        print(user_id)
        if user_id:
            return token


api = NinjaAPI(csrf=False, auth=GlobalAuth())

api.add_router("user", user_router, tags=["用户"])

urlpatterns = [path("api/", api.urls)]
