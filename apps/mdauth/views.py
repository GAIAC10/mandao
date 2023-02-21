from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from .forms import PersonForm,StudentForm
from .models import User
from .models import User
from utils import restful
from django.contrib.auth import login,logout
from django.contrib.auth.backends import ModelBackend
# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.middleware.csrf import get_token
from .decrators import cc_login_required

class MyBackend(ModelBackend):
    def authenticate(self,telephone=None,password=None):
        try:
            user = User.objects.get(telephone=telephone)
            if user.password == password:
                return user
            else:
                pwd = user.password
                if check_password(password,pwd):
                    return user
                else:
                    return None

        except Exception as e:
            print(e)
            return None

# Create your views here.
def login_index(request):
    get_token(request)
    auth = MyBackend()
    if request.method == "GET":
        return render(request, "login.html")
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get("telephone")
            try:
                logout(request, request.user)
                b = 1 + 'a'
            except Exception as e:
                print(e)
                password = form.cleaned_data.get("password")
                print(telephone,password)
                user = auth.authenticate(telephone=telephone, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        request.session.set_expiry(None)
                        if user.is_superuser:
                            return restful.ok(data="super")
                        else:
                            return restful.ok(data="None")
                    else:
                        return restful.unauth(message="你的账号已被冻结！请联系管理员！")
                else:
                    return restful.server_error(message="账号或者密码错误！")
        else:
            return restful.server_error()


