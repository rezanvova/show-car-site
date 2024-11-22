from django.contrib import admin
from .models import *
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [ 'company','name','description', 'photo', 'cat','is_published']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = [ 'name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = [ 'name']
    prepopulated_fields = {'slug': ('name',)}

