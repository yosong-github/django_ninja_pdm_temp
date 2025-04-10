from django.db import models

USER_TYPE_CHOICES = (
    (1, "普通用户"),
    (2, "管理员"),
    (3, "超级管理员"),
)


class SysUser(models.Model):
    """用户表"""

    # 可以为空
    username = models.CharField(max_length=32, verbose_name="用户名", null=True)
    password = models.CharField(max_length=32, verbose_name="密码", null=True)
    phone = models.CharField(max_length=11, verbose_name="手机号", null=True)
    email = models.CharField(max_length=32, verbose_name="邮箱", null=True)
    avatar = models.CharField(max_length=256, verbose_name="头像", null=True)
    openid = models.CharField(max_length=256, verbose_name="openid", null=True)
    unionid = models.CharField(max_length=256, verbose_name="unionid", null=True)
    user_type = models.SmallIntegerField(choices=USER_TYPE_CHOICES, verbose_name="用户类型")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    # 继承模型管理器
    objects = models.Manager()

    def __str__(self):
        return self.username

    # def meta(self):
    #     db_table = "sys_user"
    #     db_table_comment = "用户表"
