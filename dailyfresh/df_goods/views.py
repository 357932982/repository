from django.shortcuts import render


def index(request):
    return render(request, 'df_goods/index.html')


def get_list(request):
    return render(request, 'df_goods/list.html')


def cart(request):
    return render(request, 'df_goods/cart.html')


def detail(request):
    return render(request, 'df_goods/details.html')


def place_order(request):
    return render(request, 'df_goods/place_order.html')
