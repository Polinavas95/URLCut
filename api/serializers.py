from django.contrib.auth.forms import UserCreationForm
from rest_framework import serializers

from .models import CutURL, User


class CutURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = CutURL
        fields = ('origUrl', 'path', 'cutUrl')
