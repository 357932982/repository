# coding=utf-8
from django.db import models


class OrderInfo(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    order_IsPay = models.BooleanField(default=False)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    order_address = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo', on_delete=models.CASCADE)
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField()
    item_total = models.DecimalField(max_digits=6, decimal_places=2)

