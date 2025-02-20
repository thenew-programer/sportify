from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    PermissionsMixin,
    AbstractBaseUser,
)


class UserManager(BaseUserManager):
    def create_user(self, login, password=None):
        if not login:
            raise ValueError("You must provide login")

        login = login.lower()
        user = self.model(login=login)
        user.set_password(password)
        user.save()
        return user

    def create_admin(self, login, password=None):
        user = self.create_user(login, password)
        user.is_admin = True
        user.save()
        return user

    def create_superuser(self, login, password=None):
        user = self.create_user(login, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # flag for club admin users
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "login"

    def __str__(self) -> str:
        return self.login
