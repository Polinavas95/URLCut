
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Client, UrlCut
from .serializers import ClientSerializer, UrlCutSerializer
from .permission import OwnResourcePermission


class PerformCreateMixin:

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UrlCutViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = UrlCut.objects.all()
    serializer_class = UrlCutSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, OwnResourcePermission,)
    filter_backends = [filters.SearchFilter, ]
    filter_fields = ['url_original']


class ClientViewSet(PerformCreateMixin, viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, OwnResourcePermission)
