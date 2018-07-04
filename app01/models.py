from django.db import models

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
    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = "table_name"

        # 联合索引
        index_together = [
            ("pub_date", "deadline"),
        ]

        # 联合唯一索引
        unique_together = (("driver", "restaurant"),)

        # admin中显示的表名称
        # verbose_name
        #
        # # verbose_name加s
        # verbose_name_plural