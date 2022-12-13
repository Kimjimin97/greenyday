from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$') # 휴대폰 형식이 010-1234-1234, 01012341234 둘다 됨.
    phone = models.CharField(validators=[phoneNumberRegex], max_length=11, unique=True)
    is_kakao = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]