#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Data Models for blogging
"""
__author__ = "oerb"
__copyright__ = "GPL 2014"
__license__ = "GPL3"


from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User, Group
from django.utils.timezone import now
from menues.models import Menu

class Item(models.Model):
    """
    Homepage Context Items
    """
    menu_id = models.ManyToManyField(Menu, verbose_name=u'Menu_ID')
    item_subject = models.CharField(max_length=100, verbose_name=u'Subject')
    item_description = HTMLField(verbose_name=u'Description')
    item_author = models.ForeignKey(User, related_name=u'item_author')
    item_date_creation = models.DateTimeField(editable=False, auto_now_add=True, verbose_name=u'item_creation_date')
    item_date_last_edit = models.DateTimeField(editable=False, auto_now=True, verbose_name=u'item_last_edit_date')
    item_last_editor = models.ForeignKey(User, related_name=u'item_last_editor')
    item_hide = models.BooleanField()

    class Meta:
        verbose_name = u'Item'
        verbose_name_plural = u'Items'
        ordering = ['-item_date_creation']

    def __unicode__(self):
        return self.item_subject

    def save(self, *args, **kwargs):
        """
        hier wird die Methode save der Elternklasse (models.Model)
        ueberschrieben
        """
        if not self.id:
            self.item_date_creation = now()
            self.item_date_last_edit = now()
        else:
            self.item_date_last_edit = now()
        # Aufruf der save-Methode der Elternklasse
        super(Item, self).save(*args, **kwargs)
