from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from menues.models import Bilder

class BannerType(models.Model):
    """
    Hide grouped Banners
    """
    bannertype_subject = models.CharField(max_length=100, verbose_name=u'Bannertype')
    bannertype_hide = models.BooleanField(verbose_name=u'Bannertype Hide')

    def __unicode__(self):
        return self.bannertype_subject


class Position(models.Model):
    """
    Postition in base.html Template
    """
    position_name = models.CharField(max_length=100, verbose_name=u'Name',
                                     help_text='First Element is Left an Second is Right just name it as you want')

    def __unicode__(self):
        return self.position_name


class Banner(models.Model):
    """
    Banners for sidebar or else
    """
    banner_header = models.CharField(max_length=100,verbose_name=u'Header')
    bannerhtml = HTMLField(verbose_name=u'Banner Html', blank=True, null=True)
    bannerimage = models.ForeignKey(Bilder, verbose_name=u'Banner Image', blank=True, null=True)
    bannerlink = models.CharField(max_length=255, verbose_name=u'Link', blank=True, null=True)
    banner_hide = models.BooleanField(verbose_name=u'Hide')
    banner_header_hide = models.BooleanField(verbose_name=u'Hide Header')
    banner_creation_date = models.DateTimeField(editable=False, auto_now_add=True, verbose_name=u'Creation Date')
    banner_last_edit = models.DateTimeField(editable=False, auto_now=True, verbose_name=u'Last Edit')
    banner_author = models.ForeignKey(User, verbose_name=u'Author', blank=True, null=True)
    position = models.ForeignKey(Position, verbose_name=u'Template Position')
    banner_type = models.ForeignKey(BannerType, verbose_name=u'Banner Type', blank=True, null=True)

    class Meta:
        verbose_name = u'Banner'
        verbose_name_plural = u'Banners'
        ordering = ['-banner_creation_date']

    def __unicode__(self):
        return self.banner_header