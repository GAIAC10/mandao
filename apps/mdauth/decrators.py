#encoding: utf-8
from utils import restful
from django.shortcuts import redirect
from functools import wraps
from django.http import Http404

def cc_login_required(func):
    def wrapper(request,*args,**kwargs):
        # user.is_authenticated()判断用户是否登陆
        # user.is_authenticated()通过判断session中是否有user_id 以及user_backend 来判断用户是否登陆
        # if request.session['userid']:
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            if request.is_ajax():
                return restful.unauth(message='请先登录！')
            else:
                return redirect('/')
    return wrapper


def cc_superuser_required(viewfunc):
    @wraps(viewfunc)
    def decorator(request,*args,**kwargs):
        if request.user.is_superuser:
            return viewfunc(request,*args,**kwargs)
        else:
            raise Http404()
    return decorator

def cc_staff_required(viewFunc):
    @wraps(viewFunc)
    def decorator(request,*args,**kwargs):
        if request.user.is_staff:
            return viewFunc(request, *args, **kwargs)
        else:
            raise Http404()
    return decorator