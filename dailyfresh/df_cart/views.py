from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import CartInfo
from df_goods.models import GoodsInfo


def cart(request):
    user_id = request.session.get('user_id')
    cart_info = CartInfo.objects.filter(user_id=user_id)
    length = len(cart_info)
    context = {'title': '购物车', 'get_cart': 0, 'cart_info': cart_info, 'length': length}
    return render(request, 'df_cart/cart.html', context)


def place_order(request):
    return render(request, 'df_cart/place_order.html', {'title': '提交订单', 'get_cart': 0})


def add(request, id, count):
    user_id = request.session.get('user_id')
    goods_id = int(id)
    count = int(count)
    cart_info_list = CartInfo.objects.filter(user_id=user_id, goods_id=goods_id)
    if len(cart_info_list) > 0:
        cart_info = cart_info_list[0]
        cart_info.count += count
    else:
        cart_info = CartInfo()
        cart_info.count = count
        cart_info.goods_id = goods_id
        cart_info.user_id = user_id
    cart_info.save()
    # 购物车里的商品种类数
    totle = CartInfo.objects.filter(user_id=user_id).count()
    request.session['totle'] = totle
    if request.is_ajax():
        return JsonResponse({'data': totle})
    else:
        return redirect('/cart/cart/')


def change(request):
    receive = request.GET
    cart_id = receive.get('cart_id')
    count = receive.get('count')
    try:
        cart_info = CartInfo.objects.get(id=cart_id)
        count = int(count)
        print('count:',count)
        if count > 0:
            cart_info.count = count
            cart_info.save()
            data = {'info': '0'}
        else:
            data = {'info': str(cart_info.count)}
    except Exception as e:
        data = {'info': str(cart_info.count)}
        print(data)
    return JsonResponse(data)


def delete(request):
    receive = request.GET
    cart_id = receive.get('cart_id')
    try:
        cart_info = CartInfo.objects.get(id=cart_id)
        cart_info.delete()
        data = {'info': 1}
    except Exception as e:
        data = {'info': 0}
    return JsonResponse(data)
