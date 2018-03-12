from django.shortcuts import render
from df_user.models import UserInfo
from df_cart.models import CartInfo


# Create your views here.
def place_order(request):
    user_id = request.session.get('user_id')
    user = UserInfo.user.get(id=user_id)
    carts = CartInfo.objects.filter(user_id=user_id)
    context = {'title': '提交订单', 'get_cart': 0, 'user': user, 'carts': carts}
    return render(request, 'df_order/place_order.html', context)


def order_handler(request):
    post = request.POST
    address = post.get('address')
    pay_type = post.get('pay_type')
    goods_id = post.get('goods_id')
    print('address'%address)
    print('pay_type:'%pay_type)
    print('goods_id:'%goods_id)
    return render(request, 'df_order/place_order.html')