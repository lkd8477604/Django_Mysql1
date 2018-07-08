from django.db import models
from datetime import datetime
from django.utils.html import format_html
# Create your models here.
class book_autor(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    def __str__(self):
        return "%s %s" % (self.name, self.email)
class Publisher(models.Model):
    name = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    website = models.URLField()
    def __str__(self):
        return "%s" % (self.name)
class book(models.Model):
    name = models.CharField(max_length=64)
    authors = models.CharField(max_length=12)
    publisher = models.CharField(max_length=64)
    price = models.IntegerField()
    publishday = models.DateTimeField(default=datetime.now())
    status_choice = (('published', u'已出版'),
                     ('publishing', u'待出版'),
                     ('forbiden', u'禁书'),)
    statue =models.CharField(choices=status_choice, max_length=24, default='publishing')
    def __str__(self):
        return "%s" % (self.name)

    def color_status(self):
        if self.statue == 'published':
            format_td = format_html('<span style="padding:2px;background-color:green;color:white">已出版</span>')
        if self.statue == 'publishing':
            format_td = format_html('<span style="padding:2px;background-color:gray;color:white">待出版</span>')
        if self.statue == 'forbiden':
            format_td = format_html('<span style="padding:2px;background-color:red;color:white">禁书</span>')
        return format_td