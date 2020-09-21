import random
from string import ascii_letters, digits

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import viewsets, mixins, filters, generics

from .models import CutURL
from .serializers import CutURLSerializer
from .permission import OwnResourcePermission


CHOICE = ascii_letters + digits


def get_url(k: int) -> str:
    path = ''.join(random.choices(CHOICE, k=k))
    check_path = CutURL.objects.filter(path=path).first()
    if check_path:
        return get_url(k)
    return path


class PerformCreateMixin:

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




class UrlRedirect(generics.GenericAPIView):
    queryset = CutURL.objects.all()
    lookup_field = 'path'

    def get(self, request, *args, **kwargs) -> None:
        instance = self.get_object()
        return redirect(instance.origUrl)


class CutURLViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = CutURL.objects.all()
    serializer_class = CutURLSerializer
    lookup_field = 'path'
    permission_classes = (OwnResourcePermission,)
    filter_backends = [filters.SearchFilter, ]
    filter_fields = ['origUrl']

    def create(self, request, *args, **kwargs):
        path = request.data.get('path')
        origUrl = request.data.get('origUrl')
        author = request.user
        scheme = 'https://' if request.is_secure() else 'http://'
        host = request.get_host()
        if not path:
            path = get_url(k=7)
        cutUrl = f'{scheme}{host}/{path}'
        request._full_data = {'author': author, 'origUrl': origUrl, 'path': path, 'cutUrl': cutUrl}
        return super().create(request, *args, **kwargs)
