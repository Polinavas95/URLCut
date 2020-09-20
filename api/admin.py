from django.contrib import admin
from .models import Client, CutURL


class ClientAdmin(admin.ModelAdmin):
    list_display = ('author',)
    search_fields = ('author',)


class CutURLAdmin(admin.ModelAdmin):
    list_display = ('origUrl', 'cutUrl',)
    search_fields = ('origUrl',)


admin.site.register(Client, ClientAdmin)
admin.site.register(CutURL, CutURLAdmin)
