from django.shortcuts import render
from django.core.paginator import Paginator

from .models import GoodsInfo, TypeInfo


def index(request):
    type_list = TypeInfo.objects.all()
    type_01 = type_list[0].goodsinfo_set.order_by('-id')[0:4]
    type_02 = type_list[1].goodsinfo_set.order_by('-id')[0:4]
    type_03 = type_list[2].goodsinfo_set.order_by('-id')[0:4]
    type_04 = type_list[3].goodsinfo_set.order_by('-id')[0:4]
    type_05 = type_list[4].goodsinfo_set.order_by('-id')[0:4]
    type_06 = type_list[5].goodsinfo_set.order_by('-id')[0:4]
    context = {'title': '首页', 'get_cart': 1, 'type_01': type_01, 'type_02': type_02, 'type_03': type_03,
               'type_04': type_04, 'type_05': type_05, 'type_06': type_06}
    return render(request, 'df_goods/index.html', context)


def get_list(request, type, sort, index):
    typeinfo =TypeInfo.objects.get(pk=int(type))
    if sort == '1':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(type)).order_by('-id')
    if sort == '2':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(type)).order_by('-goods_price')
    if sort == '3':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(type)).order_by('-goods_click')
    new_goods = goods_list[0:3]
    paginator = Paginator(goods_list, 1)
    page = paginator.page(int(index))
    context = {'title': '商品列表', 'get_cart': 1, 'page': page, 'paginator': paginator,
               'typeinfo': typeinfo, 'new_goods': new_goods, 'sort': sort}
    return render(request, 'df_goods/list.html', context)


def cart(request):
    return render(request, 'df_goods/cart.html', {'title': '购物车', 'get_cart': 0})


def detail(request):
    return render(request, 'df_goods/detail.html', {'title': '商品详情', 'get_cart': 1})


def place_order(request):
    return render(request, 'df_goods/place_order.html', {'title': '提交订单', 'get_cart': 0})
