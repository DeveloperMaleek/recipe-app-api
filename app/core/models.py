# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    # PermissionsMixin,
)


class UserManager(BaseUserManager):
    # Manager for users.

    def create_user(self, email, password=None, **extra_fields):
        # Create, save and return a new user.
        if not email:
            raise ValueError('User must have email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class RecipeUser(AbstractBaseUser, BaseUserManager):
    # User in the system shows here
    email = models.EmailField(max_length=255, unique=True)
    users_name = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
