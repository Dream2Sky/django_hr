from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models import DO_NOTHING, SET_NULL

from apps.models import BaseDataModel


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **kwargs):
        if not username or not password:
            raise ValueError("请正确传递参数")

        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password, **kwargs):
        kwargs["is_superuser"] = False
        return self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        kwargs["is_superuser"] = True
        return self._create_user(username, password, **kwargs)


class User(BaseDataModel, AbstractBaseUser):
    class Meta(object):
        db_table = "auth_user"

    username = models.CharField(max_length=100, null=False, unique=True)
    is_superuser = models.BooleanField(default=False)

    # 被定义为username_field的字段必须设置为唯一
    USERNAME_FIELD = "username"

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
