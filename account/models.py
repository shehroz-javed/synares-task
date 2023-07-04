from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username}'


class WebLinks(models.Model):
    url = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.url}'


class Linkcount(models.Model):
    url = models.OneToOneField(WebLinks, on_delete=models.CASCADE)
    visit_count = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    updated_at = models.DateTimeField(default=None)

    def __str__(self):
        return f'{self.url}----{self.visit_count}----{self.user}-----{self.updated_at}'
