from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True
    )
    city = models.CharField(max_length=200, verbose_name="Город", blank=True, null=True)
    token = models.CharField(
        max_length=100, verbose_name="токен", blank=True, null=True
    )
    tg_id = models.CharField(
        max_length=50, verbose_name="номер телеграм чата ", blank=True, null=True
    )
    is_active = models.BooleanField(
        blank=True, null=True, verbose_name="", help_text=""
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
