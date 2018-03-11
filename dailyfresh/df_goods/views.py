from django.shortcuts import render
from django.core.paginator import Paginator

from .models import GoodsInfo, TypeInfo
from df_cart.models import CartInfo


def index(request):
    user_id = request.session.get('user_id')
    type_list = TypeInfo.objects.all()
    type_01 = type_list[0].goodsinfo_set.order_by('-id')[0:4]
    type_02 = type_list[1].goodsinfo_set.order_by('-id')[0:4]
    type_03 = type_list[2].goodsinfo_set.order_by('-id')[0:4]
    type_04 = type_list[3].goodsinfo_set.order_by('-id')[0:4]
    type_05 = type_list[4].goodsinfo_set.order_by('-id')[0:4]
    type_06 = type_list[5].goodsinfo_set.order_by('-id')[0:4]
    totle = CartInfo.objects.filter(user_id=user_id).count()
    request.session['totle'] = totle
    context = {'title': '首页', 'get_cart': 1, 'type_01': type_01, 'type_02': type_02, 'type_03': type_03,
               'type_04': type_04, 'type_05': type_05, 'type_06': type_06}
    return render(request, 'df_goods/index.html', context)


def get_list(request, type, sort, index):
    typeinfo = TypeInfo.objects.get(pk=int(type))
    if sort == '1':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(type)).order_by('-id')
    if sort == '2':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(type)).order_by('-goods_price')
    if sort == '3':
        goods_list = GoodsInfo.objects.filter(goods_type_id=int(type)).order_by('-goods_click')
    new_goods = goods_list[0:3]
    paginator = Paginator(goods_list, 5)
    page = paginator.page(int(index))
    context = {'title': '商品列表', 'get_cart': 1, 'page': page, 'paginator': paginator,
               'typeinfo': typeinfo, 'new_goods': new_goods, 'sort': sort}
    return render(request, 'df_goods/list.html', context)


def detail(request, type, id):
    typeinfo = TypeInfo.objects.get(pk=int(type))
    goods = GoodsInfo.objects.get(id=id)
    new_goods = GoodsInfo.objects.filter(goods_type_id=goods.goods_type_id).order_by('-id')[0:3]
    context = {'title': '商品详情', 'get_cart': 1, 'goods': goods, 'new_goods': new_goods, 'typeinfo': typeinfo}
    response = render(request, 'df_goods/detail.html', context)
    # 保存goods_id信息到cookie中
    goods_ids = request.COOKIES.get('goods_ids', -1)
    if goods_ids != -1:
        goods_id_list = goods_ids.split(',')
        if goods_id_list.count(id) >= 1:
            goods_id_list.remove(id)
        goods_id_list.insert(0, id)
        if len(goods_id_list) >= 6:
            del goods_id_list[5]
        goods_ids = ','.join(goods_id_list)
    else:
        goods_ids = id
    response.set_cookie('goods_ids', goods_ids)
    return response
