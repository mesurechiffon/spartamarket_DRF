from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender_choice = [("m", "남성"), ("f", "여성")]

    nickname = models.CharField(max_length=50)
    birth = models.DateField()

    # 선택필드
    gender = models.CharField(
        max_length=1, choices=gender_choice, null=True, blank=True
        )
    introduction = models.TextField(default="")
