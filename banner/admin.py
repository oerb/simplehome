__author__ = 'oerb'

from django.contrib import admin
from banner.models import Banner, Position, BannerType

class BannerAdmin(admin.ModelAdmin):
    """
    For nice Menu
    """
    list_display = ('banner_header', 'bannerimage', 'position', 'banner_type')
    list_filter = ('banner_creation_date',)
    search_fields = ('banner_header', 'bannerimage')


# TODO: Position and BannerType hide in Admin Mainpage but adding is on in Banner Adminsite
# Registrationpart
admin.site.register(Banner, BannerAdmin)
admin.site.register(Position)
admin.site.register(BannerType)

