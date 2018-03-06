from django.shortcuts import render


def index(request):
    return render(request, 'df_goods/index.html', {'title': '首页'})


def get_list(request):
    return render(request, 'df_goods/list.html', {'title': '商品列表'})


def cart(request):
    return render(request, 'df_goods/cart.html', {'title': '购物车'})


def detail(request):
    return render(request, 'df_goods/detail.html', {'title': '商品详情'})


def place_order(request):
    return render(request, 'df_goods/place_order.html', {'title': '提交订单'})
