from django.contrib import admin

# Register your models here.
from app01 import models

def statue_action(modelAdmin, request, queryset):
    print ('---<', request, queryset)
    queryset.update(statue = 'forbiden')
    statue_action.short_description = 'Set to forbiden'

class book_model(admin.ModelAdmin):
    list_display = ('id', 'name', 'authors', 'publisher', 'publishday', 'color_status')
    list_filter = ('authors', 'publishday')
    search_fields = ('name', 'publisher')
    # list_editable = ('name','authors', 'publisher', 'publishday')
    actions = [statue_action,]
admin.site.register(models.book, book_model)
admin.site.register(models.book_autor)
admin.site.register(models.Publisher)
