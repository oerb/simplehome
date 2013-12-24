__author__ = 'oerb'

from django.contrib import admin
from banner.models import Banner, Position, BannerType

# TODO: Position and BannerType hide in Admin Mainpage but adding is on in Banner Adminsite
# Registrationpart
admin.site.register(Banner)
admin.site.register(Position)
admin.site.register(BannerType)

