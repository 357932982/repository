from re import compile

from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import deprecation

EXEMPT_URLS = []
print(hasattr(settings, 'LOGIN_EXEMPT_URLS'))
if hasattr(settings, "LOGIN_EXEMPT_URLS"):
    # 把需要匹配的url表达是存入list中
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class Validate(deprecation.MiddlewareMixin):
    def process_request(self, request):
        user_id = request.session.get('user_id')
        print(user_id)
        if user_id is None:
            path = request.path_info.lstrip('/')
            # 匹配不到的url就跳转到登录页面,any()中如果有部分匹配，则返回True,否则返回False
            if not any(m.match(path) for m in EXEMPT_URLS):
                print(path)
                return HttpResponseRedirect('/user/login/')
