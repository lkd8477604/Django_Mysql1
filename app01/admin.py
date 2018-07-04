from django.contrib import admin

# Register your models here.
from app01 import models

admin.site.register(models.book)
admin.site.register(models.book_autor)
admin.site.register(models.Publisher)
