__author__ = 'oerb'

from django.contrib import admin
from menues.models import Menu, Bilder, MetaInfos

class MenuAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('subject', 'parent', 'level', 'menu_hide')
    list_filter = ('menu_hide', 'level')
    search_fields = ('subject',)


class MetaInfosAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('metainfo_subject', 'metainfo')


class BilderAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('bild_subject', 'bild_file')
    search_fields = ('bild_subject', 'bild_file')


# Registrationpart
admin.site.register(Menu, MenuAdmin)
admin.site.register(Bilder, BilderAdmin)
admin.site.register(MetaInfos, MetaInfosAdmin)
