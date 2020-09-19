from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.shortcuts import render, get_object_or_404

from .models import Client, UrlCut


class ClientSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Client
        fields = '__all__'


class UrlCutSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrlCut
        fields = '__all__'
        unique_together = ('url_original', 'url_cut')
        validators = [
            UniqueTogetherValidator(
                queryset=UrlCut.objects.all(),
                fields=['url_original', 'url_cut']
            )
        ]

    def get_short_url(self, url):
        url_original = get_object_or_404(UrlCut, url_original=url)
        url_cut = ''
        for i in range(len(url_original)):
            if url_cut.find(url_original[i]) == -1:
                url_cut += url_original[i]
        return url_cut