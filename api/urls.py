from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CutURLViewSet, UrlRedirect

router = DefaultRouter()
router.register(r'urls', CutURLViewSet, basename='urls')

urlpatterns = [
    path('', include(router.urls)),
    path('<str:path>', UrlRedirect.as_view()),
]

