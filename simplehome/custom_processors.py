# Custom Context_Processors
from menues.models import Menu, MetaInfos
from banner.models import Banner

def menulist(request):
    """                                                                         
    A context processor that provides 'menu' for base HTML
    by a special line in settings.py                                    
    """                                                                         
    menulist = Menu.objects.filter(level=1)
    return { 'menulist': menulist }

def level2menulist(request):
    level2menulist= Menu.objects.filter(level=2)
    return  { 'level2menulist':level2menulist }

def bannerlist_left(request):
    """
    Bannerlist Right
    ( base.html alignement by
    """
    bannerlist_left = Banner.objects.filter(position=1).filter(banner_hide=False)
    return {'bannerlist_left':bannerlist_left}

def bannerlist_right(request):
    """
    Bannerlist Right
    ( base.html alignement by
    """
    bannerlist_right = Banner.objects.filter(position=2).filter(banner_hide=False)
    return {'bannerlist_right':bannerlist_right}

def footer(request):
    """
    Base.html Footer out auf MetaInfos
    """
    footer = MetaInfos.objects.filter(metainfo_subject='footer')
    return {'footer':footer}

def metainfos_author(request):
    """
    Base.html Meta author
    """
    author = MetaInfos.objects.filter(metainfo_subject="author")
    if author:
        for e in author:
            metainfo_author = e.metainfo
    else:
        metainfo_author = ''
    return {'metainfo_author':metainfo_author}

def metainfos_keywords(request):
    """
    Base.html Meta Keywords
    """
    keywords = MetaInfos.objects.filter(metainfo_subject="keywords")
    if keywords:
        for e in keywords:
            metainfo_keywords = e.metainfo
    else:
        metainfo_keywords = ''
    return {'metainfo_keywords':metainfo_keywords}

def metainfos_descriptions(request):
    """
    Base.html Meta descriptions
    """
    descriptions = MetaInfos.objects.filter(metainfo_subject="description")
    if descriptions:
        for e in descriptions:
            metainfo_descriptions = e.metainfo
    else:
        metainfo_descriptions = ''
    return {'metainfo_descriptions':metainfo_descriptions}
