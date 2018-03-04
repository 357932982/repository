# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .models import UserInfo
from hashlib import sha1


def register(request):
    return render(request, 'df_user/register.html', {'title': '注册'})


# 处理注册信息
def register_handler(request):
    # 接收用户信息
    user_name = request.POST['user_name']
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
    user_name = request.COOKIES.get('user_name', '')
    context = {'title': '登录', 'user_name': user_name}
    return render(request, 'df_user/login.html', context)


def logout(request):
    del request.session['user_name']
    return HttpResponseRedirect('/user/login')


def login_handler(request):
    post = request.POST
    user_name = post.get('username')
    pwd = post.get('pwd')
    remember = post.get('remember', '0')
    users = UserInfo.user.filter(user_name=user_name)
    if 1 == len(users):
        s1 = sha1()
        s1.update(pwd.encode('utf-8'))
        pwd1 = s1.hexdigest()
        if pwd1 == users[0].user_password:
            red = HttpResponseRedirect('/user/info')
            if '1' == remember:
                red.set_cookie('user_name', user_name)
            else:
                red.set_cookie('user_name', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = user_name
            request.session['user_email'] = users[0].user_email
            return red
        else:
            context = {'title': '登录', 'error_user': '0', 'error_pwd': '1', 'user_name': user_name, 'pwd': pwd}
            return render(request, 'df_user/login.html', context)

    context = {'title': '登录', 'error_user': '1', 'error_pwd': '0', 'user_name': user_name, 'pwd': pwd}
    return render(request, 'df_user/login.html', context)


# 转到个人中心
def info(request):
    return render(request, 'df_user/user_center_info.html', {'title': '用户中心'})


# 转到订单详情页
def order(request):
    return render(request, 'df_user/user_center_order.html', {'title': '用户中心'})


# 转到收货地址页
def site(request):
    user_id = request.session.get('user_id')
    users = UserInfo.user.filter(id=user_id)
    receiver = users[0].receiver
    receiver_address = users[0].receiver_address
    receiver_post = users[0].receiver_post
    receiver_phone = users[0].receiver_phone
    if receiver == '' or receiver_address == '' or receiver_phone == '' or receiver_post == '':
        address_info = '没有数据！'
    else:
        address_info = receiver_address + '(' + receiver + '收)' + receiver_phone
        print(address_info)
    context = {'title': '用户中心', 'address_info': address_info}
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
