from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CutURLViewSet, ClientViewSet

router = DefaultRouter()

router.register(r'clients', ClientViewSet, basename='client')
router.register(r'http://127.0.0.1:8000/u/(?P<id>[0-9]+)/(?P<slug>[\w]+)/$', CutURLViewSet, basename='url')

urlpatterns = [
    path('', include(router.urls)),
]

