from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Client(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class UrlCut(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    url_original = models.URLField()
    url_cut = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
