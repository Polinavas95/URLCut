from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Client(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class UrlCut(models.Model):
    url_original = models.SlugField(unique=True)
    url_cut = models.SlugField(unique=True)
