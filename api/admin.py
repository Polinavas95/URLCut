from django.conf.urls import url
from django.contrib import admin
from .models import Client, UrlCut


class ClientAdmin(admin.ModelAdmin):
    list_display = ('author',)
    search_fields = ('author',)
    list_filter = ('author',)


class UrlCutAdmin(admin.ModelAdmin):
    list_display = ('url_original', 'url_cut',)
    search_fields = ('url_original',)
    empty_value_display = '-пусто-'


admin.site.register(Client, ClientAdmin)
admin.site.register(UrlCut, UrlCutAdmin)
