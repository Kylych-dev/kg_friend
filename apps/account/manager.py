from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_manager(self, email, password=None, **extra_fields):
    #     return self.create_user(
    #         email,
    #         role='manager',
    #         password=password,
    #         **extra_fields
    #     )
    #
    # def create_userprofile(self, email, password=None, **extra_fields):
    #     return self.create_user(
    #         email,
    #         role='user',
    #         password=password,
    #         **extra_fields
    #     )

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)