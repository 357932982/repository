from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import transaction
from df_user.models import UserInfo
from df_cart.models import CartInfo
from .models import OrderInfo, OrderDetailInfo

from datetime import datetime


# Create your views here.
def place_order(request):
    user_id = request.session.get('user_id')
    user = UserInfo.user.get(id=user_id)
    carts = CartInfo.objects.filter(user_id=user_id)
    context = {'title': '提交订单', 'get_cart': 0, 'user': user, 'carts': carts}
    return render(request, 'df_order/place_order.html', context)


@transaction.atomic()
def order_handler(request):
    tran_id = transaction.savepoint()
    post = request.POST
    address = post.get('address')
    pay_type = post.get('pay_type')
    total_pay = post.get('total_pay')
    cart_id_list = post.get('cart_id_list')
    try:
        # 创建订单对象
        order = OrderInfo()
        now = datetime.now()
        user_id = request.session['user_id']
        order.order_id = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), user_id)
        order.order_date = now
        order.user_id = user_id
        order.order_address = address
        order.order_total = total_pay
        order.save()
        print(cart_id_list)
        cart_ids = [int(item) for item in cart_id_list.split(',')]
        for cart_id in cart_ids:
            detail = OrderDetailInfo()
            detail.order = order
            # 查询购物车信息
            cart = CartInfo.objects.get(id=cart_id)
            # 判断商品库存
            goods = cart.goods
            # 如果商品库存大于购物车商品数量，减少库存
            if goods.goods_count > cart.count:
                goods.goods_count = goods.goods_count - cart.count
                goods.save()
                # 完善订单信息
                detail.goods_id = goods.id
                detail.price = goods.goods_price
                detail.count = cart.count
                detail.item_total = detail.price * detail.count
                detail.save()
                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)
                return JsonResponse({'data': 0})
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print('*' * 30)
        print(e)
        print('*' * 30)
        transaction.savepoint_rollback(tran_id)
    return JsonResponse({'data': 1})


@transaction.atomic()
def pay(request):
    post = request.POST
    order_id = post.get('order_id')
    order = OrderInfo.objects.get(order_id=order_id)
    tranc_id = transaction.savepoint()
    money = order.order_total
    try:
        order.order_IsPay = True
        order.save()
        transaction.savepoint_commit(tranc_id)
    except Exception as e:
        transaction.savepoint_rollback(tranc_id)
        print('*' * 30)
        print(e)
        print('*' * 30)
    return JsonResponse({'money': money, 'state': order.order_IsPay})
