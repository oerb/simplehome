__author__ = 'oerb'

from django.contrib import admin
from blog.models import Item

class ItemAdmin(admin.ModelAdmin):
    """
    For excluding date- and authorfields and fill them at savetime
    """
    list_display = ('item_subject', 'item_date_creation', 'item_date_last_edit', 'item_author' )
    list_filter = ('item_date_last_edit', 'item_date_creation')
    #search_fields = ('item_subject')
    exclude = ('item_date_last_edit', 'item_date_cr   eation', 'item_last_editor', 'item_author')
    def save_model(self, request, obj, form, change):
        if obj.id:
            obj.item_last_editor = request.user

        else:
            obj.item_author = request.user
            obj.item_last_editor = request.user

        obj.save()

# Registrationpart
admin.site.register(Item, ItemAdmin)

