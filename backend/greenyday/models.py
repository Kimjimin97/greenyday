from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MEta:
        abstract = True

class Menu(TimestampedModel):
    photo = models.ImageField(upload_to="greenyday/menu/%Y/%m/%d")
    name = models.CharField(max_length=100, unique=True)
    caption = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Review(TimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="greenyday/review/%Y/%m/%d")
    menu_name = models.ForeignKey(Menu, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=500)