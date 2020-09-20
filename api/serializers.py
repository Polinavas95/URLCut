from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.shortcuts import render, get_object_or_404

from .models import Client, CutURL


class ClientSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Client
        fields = '__all__'


class CutURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = CutURL
        fields = '__all__'
        unique_together = ('origUrl', 'cutUrl')
        validators = [
            UniqueTogetherValidator(
                queryset=CutURL.objects.all(),
                fields=['origUrl', 'cutUrl']
            )
        ]

    def get_short_url(self, url):
        origUrl = get_object_or_404(CutURL, origUrl=url)
        cutUrl = ''
        for i in range(len(origUrl)):
            if cutUrl.find(origUrl[i]) == -1:
                cutUrl += origUrl[i]
        return cutUrl

    def create(self, validated_data):
        return CutURL.objects.create(**validated_data)
