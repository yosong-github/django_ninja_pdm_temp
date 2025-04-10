from django.db import models

USER_TYPE_CHOICES = (
    (1, "普通用户"),
    (2, "管理员"),
    (3, "超级管理员"),
)


class Dsaf(models.Model):
    """用户表"""

    # 可以为空
    username = models.CharField(max_length=32, verbose_name="用户名", null=True)

    # 继承模型管理器
    objects = models.Manager()

    def __str__(self):
        return self.username

    # def meta(self):
    #     db_table = "sys_user"
    #     db_table_comment = "用户表"
