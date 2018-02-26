# coding=utf-8
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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
    pwd = s1.hexdigest()
    user = UserInfo.user.create_user(user_name, pwd, email)

    return HttpResponse(pwd)


def user_name_validate(request):
    name = request.GET['name']
    count = UserInfo.user.filter(user_name=name).count()
    print(count)
    return HttpResponse(count)


def login(request):
    return render(request, 'df_user/login.html', {'title': '登录'})


def login_handler(request):
    post = request.POST
    user_name = post.get('username')
    pwd = post.get('pwd')
    remember = post.get('remember', None)
    name = UserInfo.user.filter(user_name=user_name)
    if 0 == len(name):
        error_user = True
        context = {'title': '登录', 'error_user': error_user, 'user_name': user_name, 'pwd': pwd}
        return render(request, 'df_user/login.html', context)
        
    return HttpResponse('%s, %s, %s' % (user_name, pwd, remember))


def info(request):
    return render(request, 'df_user/user_center_info.html', {'title': '用户中心'})


def order(request):
    return render(request, 'df_user/user_center_order.html', {'title': '用户中心'})


def site(request):
    return render(request, 'df_user/user_center_site.html', {'title': '用户中心'})
