from django.contrib import admin
from .models import CutURL


class CutURLAdmin(admin.ModelAdmin):
    list_display = ("origUrl", "cutUrl", "author", "path", "created_at")
    search_fields = ("origUrl", "author", "created_at")


admin.site.register(CutURL, CutURLAdmin)
