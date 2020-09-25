from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("", include("users.urls")),
    path("", include("django.contrib.auth.urls")),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)

urlpatterns += staticfiles_urlpatterns()