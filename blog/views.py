
# ccc Veranstaltung aus Gespraechsfetzen - die waren auch aufm Gore


from blog.models import Item, Menu
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.template import RequestContext


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def mainpage(request):
    items = Item.objects.all().filter(item_hide=False).order_by('-item_date_creation')
    #if len(items) >= 5:
    #    items = items[0:4]

    #image_data = open("~/Dokumente/projekte/django/homepage/static/menu/images/avatar-15.jpg", "rb").read()
    return render_to_response('blog/mainpage.html',
        {'items':items}, context_instance=RequestContext(request))

def index(request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        if item.item_hide:
            #for hiding by Hide-Index
            return render_to_response('blog/index.html',
                {'item':None},context_instance=RequestContext(request))
        else:
            return render_to_response('blog/index.html',
                    {'item':item},context_instance=RequestContext(request))

def blog_level0(request, choice_id):
    itemlist_byMenu_id = Item.objects.filter(menu_id = choice_id).filter(item_hide=False)
    itemlist_byMenu_id = list(chunks(itemlist_byMenu_id,3))
    menuchoice = Menu.objects.get(pk=choice_id)
    return render_to_response('blog/blog_level0.html', {'menuchoice': menuchoice ,
                                                        'itemlist_byMenu_id':itemlist_byMenu_id},
                                                        context_instance=RequestContext(request))

def blog_level1(request, choice_id):
    menu = get_object_or_404(Menu, pk=choice_id)
    menues = Menu.objects.filter(parent_id = menu.id)
    menuesid = [choice_id]
    for e in menues:
        menuesid.append(e.id)
    itemlist_byMenu_id = Item.objects.filter(menu_id__in = menuesid).filter(item_hide=False)
    itemlist_byMenu_id = list(chunks(itemlist_byMenu_id,3))
    menuchoice = Menu.objects.get(pk=choice_id)
    return render_to_response('blog/blog_level1.html', {'menuchoice': menuchoice ,
                                                        'itemlist_byMenu_id':itemlist_byMenu_id},
                                                        context_instance=RequestContext(request))



