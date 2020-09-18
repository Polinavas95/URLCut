from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UrlCutViewSet, ClientViewSet

router = DefaultRouter()

router.register(r'clients', ClientViewSet, basename='Client')
router.register(r'(a-zA-Z0-9){6}', UrlCutViewSet, basename='URL')


urlpatterns = [
    path('url_cut/', include(router.urls)),
]

