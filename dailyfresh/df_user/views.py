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
    # user = UserInfo.user.create_user(user_name, pwd, email)

    return HttpResponse(pwd)


def user_name_validate(request):
    name = request.GET['name']
    count = UserInfo.user.filter(user_name=name).count()
    print(count)
    return HttpResponse(count)
