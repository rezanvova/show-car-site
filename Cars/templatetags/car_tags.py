from django import template
from Cars.models import Categories,Tags
from Cars.utils import menu

register = template.Library()

@register.inclusion_tag('cars/list_categories.html')
def show_categories(cat_selected=0):
    cats = Categories.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
@register.inclusion_tag('cars/list_tags.html')
def show_tags(tag_selected=0):
    tags = Tags.objects.all()
    return {'tags': tags, 'tag_selected': tag_selected}

@register.simple_tag()
def get_menu():
    return menu