import random
from string import ascii_letters, digits

from django.shortcuts import get_object_or_404, redirect
from requests import Response
from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Client, CutURL
from .serializers import ClientSerializer, CutURLSerializer
from .permission import OwnResourcePermission


class PerformCreateMixin:

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CutURLViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = CutURL.objects.all()
    serializer_class = CutURLSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, OwnResourcePermission,)
    filter_backends = [filters.SearchFilter, ]
    filter_fields = ['origUrl']

    CHOICE = ascii_letters + digits

    def get_random_url(self, k=7):
        return ''.join(random.choices(self.CHOICE, k=k))

    def get_cut_url(self):
        cut_url = self.get_random_url()
        check = CutURL.objects.get(cutUrl=cut_url)
        if check:
            return self.get_cut_url()
        return cut_url

    def create(self, request, *args, **kwargs):
        cut_url = request.data.get('cutUrl')
        serializer = self.serializer_class
        if cut_url:
            if serializer.is_valid():
                serializer.save(**request.data)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer,
                status=status.HTTP_400_BAD_REQUEST
            )
        request.data['cutUrl'] = self.get_cut_url()
        serializer.save(**request.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def retrieve(self, request, pk):
        url = CutURL.objects.get('origUrl').filter(pk=pk)
        return redirect(url)


class ClientViewSet(PerformCreateMixin, viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, OwnResourcePermission)
