from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class CutURL(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    origUrl = models.URLField()
    cutUrl = models.URLField(unique=True)
    path = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
