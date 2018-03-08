from django.db import models

from tinymce.models import HTMLField


class TypeInfo(models.Model):
    type_name = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.type_name


class GoodsInfo(models.Model):
    goods_name = models.CharField(max_length=20)
    goods_picture = models.ImageField(upload_to='df_goods')
    goods_comment = models.CharField(max_length=100)
    goods_price = models.DecimalField(max_digits=5, decimal_places=2)
    goods_count = models.IntegerField()
    goods_unity = models.CharField(max_length=20, default='500g')
    goods_tips = HTMLField()
    goods_click = models.IntegerField()
    is_delete = models.BooleanField(default=False)
    goods_type = models.ForeignKey('TypeInfo', on_delete=models.CASCADE)

