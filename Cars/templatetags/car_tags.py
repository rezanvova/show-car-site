from django import template
# from Cars.models import Category, TagPost
from Cars.utils import menu

register = template.Library()

# @register.inclusion_tag('cars/list_categories.html')
# def show_categories(cat_selected=0):
#     cats = Category.objects.all()
#     return {'cats':cats,'cat_selected':cat_selected}
#
#
# @register.inclusion_tag('cars/list_tags.html')
# def show_all_tags():
#     return {'tags':TagPost.objects.all()}

@register.simple_tag()
def get_menu():
    return menu