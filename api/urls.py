from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CutURLViewSet, UrlRedirect, CustomAuthToken

router = DefaultRouter()
router.register(r'urls', CutURLViewSet, basename='urls')

urlpatterns = [
    path('', include(router.urls)),
    path(r'^api-token-auth', CustomAuthToken.as_view()),
    path('<str:path>', UrlRedirect.as_view()),
]

