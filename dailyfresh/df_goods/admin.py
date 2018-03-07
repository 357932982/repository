from django.contrib import admin

from .models import GoodsInfo, TypeInfo


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods_name', 'goods_price', 'goods_unity', 'goods_count', 'goods_click', 'goods_comment']


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
