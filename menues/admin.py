__author__ = 'oerb'

from django.contrib import admin
from menues.models import Menu, Bilder, MetaInfos

# Registrationpart
admin.site.register(Menu)
admin.site.register(Bilder)
admin.site.register(MetaInfos)
