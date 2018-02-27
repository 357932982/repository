# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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
    user = UserInfo.user.create_user(user_name, pwd1, email)

    return HttpResponse(pwd)


def user_name_validate(request):
    name = request.GET['name']
    count = UserInfo.user.filter(user_name=name).count()
    print(count)
    return HttpResponse(count)


def login(request):
    user_name = request.COOKIES.get('user_name', '')
    context = {'title': '登录', 'user_name': user_name}
    return render(request, 'df_user/login.html', context)


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
        if pwd1 == users[0].pwd:
            red = HttpResponseRedirect('/user/info')
            if '1' == remember:
                red.set_cookie('user_name', user_name)
            else:
                red.set_cookie('user_name', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = user_name
            return red
        else:
            context = {'title': '登录', 'error_user': '0', 'error_pwd': '1', 'user_name': user_name, 'pwd': pwd}
            return render(request, 'df_user/login.html', context)

    context = {'title': '登录', 'error_user': '1', 'error_pwd': '0', 'user_name': user_name, 'pwd': pwd}
    return render(request, 'df_user/login.html', context)



def info(request):
    return render(request, 'df_user/user_center_info.html', {'title': '用户中心'})


def order(request):
    return render(request, 'df_user/user_center_order.html', {'title': '用户中心'})


def site(request):
    return render(request, 'df_user/user_center_site.html', {'title': '用户中心'})
