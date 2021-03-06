# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import UserInfo
from df_goods.models import GoodsInfo
from df_order.models import OrderInfo, OrderDetailInfo
from hashlib import sha1


def register(request):
    return render(request, 'df_user/register.html', {'title': '注册'})


# 处理注册信息
def register_handler(request):
    # 接收用户信息
    user_name = request.POST['user_name']
    print(user_name)
    pwd = request.POST['pwd']
    email = request.POST['email']
    # 密码加密
    s1 = sha1()
    s1.update(pwd.encode('utf-8'))
    pwd1 = s1.hexdigest()
    UserInfo.user.create_user(user_name, pwd1, email)
    red = HttpResponseRedirect('/user/login')
    red.set_cookie('user_name', user_name)
    return red


def user_name_validate(request):
    name = request.GET['name']
    count = UserInfo.user.filter(user_name=name).count()
    print(count)
    return HttpResponse(count)


def login(request):
    request.session.clear()
    user_name = request.COOKIES.get('user_name', '')
    context = {'title': '登录', 'user_name': user_name}
    # context = {'title': '登录'}
    return render(request, 'df_user/login.html', context)


def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/user/login')


def login_handler(request):
    post = request.POST
    user_name = post.get('username', '')
    print('user_name: %s' % user_name)
    pwd = post.get('pwd', '')
    remember = post.get('remember', '0')
    users = UserInfo.user.filter(user_name=user_name)
    print("users:", users)
    print('数据库查询出来的：%s' % users[0].user_name.encode("utf-8"))
    if 1 == len(users):
        s1 = sha1()
        s1.update(pwd.encode('utf-8'))
        pwd1 = s1.hexdigest()
        if pwd1 == users[0].user_password:
            red = HttpResponseRedirect('/user/info')
            if '1' == remember:
                # python2中这里一定要设置编码格式，不然报错
                red.set_cookie('user_name', user_name)
            else:
                red.set_cookie('user_name', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = user_name
            request.session['user_email'] = users[0].user_email
            print('hhh')
            return red
        else:
            context = {'title': '登录', 'error_user': '0', 'error_pwd': '1', 'user_name': user_name, 'pwd': pwd}
            return render(request, 'df_user/login.html', context)

    context = {'title': '登录', 'error_user': '1', 'error_pwd': '0', 'user_name': user_name, 'pwd': pwd}
    return render(request, 'df_user/login.html', context)


# 转到个人中心
def info(request):
    user_id = request.session.get("user_id")
    goods_ids = request.COOKIES.get('%s_goods_ids' % user_id, -1)
    goods_list = []
    if goods_ids != -1:
        goods_id_list = goods_ids.split(',')
        for goods_id in goods_id_list:
            goods = GoodsInfo.objects.get(id=goods_id)
            goods_list.append(goods)
    context = {'title': '用户中心', 'get_cart': 0, 'goods_list': goods_list}
    return render(request, 'df_user/user_center_info.html', context)


# 转到订单详情页
def order(request, index):
    user_id = request.session.get('user_id')
    order_list = []
    # 获取订单集合
    orders = OrderInfo.objects.filter(user_id=user_id).order_by('-order_date')
    # 获取订单详情
    for item in orders:
        details = OrderDetailInfo.objects.filter(order_id=item.order_id)
        order_dict = {'order': item, 'details': details}
        order_list.append(order_dict)
    paginator = Paginator(order_list, 3)
    page = paginator.page(int(index))
    context = {'title': '用户中心', 'get_cart': 0, 'order_list': order_list, 'paginator': paginator, 'page': page}
    return render(request, 'df_user/user_center_order.html', context)


# 转到收货地址页
def site(request):
    user_id = request.session.get('user_id')
    user = UserInfo.user.get(id=user_id)
    context = {'title': '用户中心', 'get_cart': 0, 'user': user}
    return render(request, 'df_user/user_center_site.html', context)


def address_handler(request):
    user_id = request.session.get('user_id')
    post = request.POST
    receiver = post.get('receiver')
    address = post.get('address')
    receiver_post = post.get('post_add')
    print(receiver_post)
    receiver_phone = post.get('phone')
    UserInfo.user.filter(id=user_id).update(receiver=receiver, receiver_address=address, receiver_post=receiver_post,
                                            receiver_phone=receiver_phone)
    return HttpResponseRedirect('/user/site/')
