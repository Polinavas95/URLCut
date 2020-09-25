from rest_framework import serializers

from .models import CutURL


class CutURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CutURL
        fields = ("origUrl", "path", "cutUrl")
