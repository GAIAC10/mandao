from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from mandao import settings
from . import forms
from . import models
from utils import restful
from . import models
import os
from django.views.decorators.http import require_POST,require_GET
# Create your views here.
from .forms import ContactForm
from .models import MachineTime, News, CommentNews
from .serializable import CommentSerizlizer
from ..cms.models import Comment, Company
from ..mdauth.models import User

def index(request):
    banners = models.MdImg.objects.all().order_by('id')[:4]
    news = News.objects.all().order_by('-time')[:3]
    context = {
        'banners': banners,
        'news': news
    }
    return render(request, "choose.html", context=context)

class contact(View):
    def get(self,request):
        company = Company.objects.all().get()
        context = {
            'telephone': company.telephone,
            'email': company.Email,
            'addr': company.addr
        }
        return render(request,'contact.html')

    def post(self,request):
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get("telephone")
            content = form.cleaned_data.get("content")
            user = User.objects.filter(telephone=telephone)
            obj = user[0]
            if obj.comment_id:
                Comment.objects.filter(id=obj.comment_id).update(content=content)
                return restful.ok()
            else:
                content = Comment.objects.create(content=content)
                user.comment = content
                user.save()
                return restful.ok()
        else:
            print(form.errors)
            return restful.params_error()

# 上传文件
# 1.在前端中
# <form enctype="multipart/form-data" action="/xxx/" method="post">
#    <input type="file" name="myfile" />
#    <input type="submit" value="upload"/>
# </form>
# 2.在views中
# request.FILES.get("myfile", None)
def upload(request):
    file = request.FILES.get('file')
    with open(os.path.join(settings.MEDIA_ROOT,file.name), 'wb') as f:
        for i in file:
            f.write(i)
    url = request.build_absolute_uri(settings.MEDIA_URL + file.name)
    return restful.ok(data=url)

def add_banners(request):
    form = forms.Img(request.POST)
    if form.is_valid():
        image_url = form.cleaned_data.get('img')
        link = form.cleaned_data.get('link')
        youxian = form.cleaned_data.get('youxian')
        banner_desc = form.cleaned_data.get("banner_desc")
        name = form.cleaned_data.get('name')
        banner = models.MdImg.objects.create(img=image_url,link=link,youxian=youxian,desc=banner_desc,name=name)
        return restful.result(data={"banner_id": banner.pk})
    else:
        print(form.errors)
        return restful.params_error(message=form.get_errors())

def works(request):
    return render(request,'works.html')

def work_detail(request):
    return render(request,'work_detail.html')

class choose(View):
    def get(self,request):
        return render(request,'choose.html')
    def post(self,request):
        # onetime = request.POST.get("onetime")
        # twotime = request.POST.get("twotime")
        # threetime = request.POST.get("threetime")
        # b1v1 = request.POST.get('b1v1')

        # eval()函数用来执行一个字符串表达式，并返回表达式的值
        a = eval(str(request.body,encoding='utf-8'))
        data = a['data']

        user = User.objects.get(uid=data['username'])
        if user:
            print(user.username)
            # data={'b1t':b1t,'b2t':b2t,'username': uid1}
            for index, value in data.items():
                if value == 'name':
                    data[index] = 0
            if user.machine_time:
                print(data['b2v1'])
                print(user.machine_time.twob2v1)
                user.machine_time.onetime = data['b1t']
                user.machine_time.twotime = data['b2t']
                user.machine_time.threetime = data['b3t']

                user.machine_time.oneb1v1 = data['b1v1']
                user.machine_time.oneb1v2 = data['b1v2']
                user.machine_time.oneb1v3 = data['b1v3']
                user.machine_time.oneb1v4 = data['b1v4']
                user.machine_time.oneb1v5 = data['b1v5']
                user.machine_time.oneb1v6 = data['b1v6']

                user.machine_time.twob2v1 = data['b2v1']
                user.machine_time.twob2v2 = data['b2v2']
                user.machine_time.twob2v3 = data['b2v3']
                user.machine_time.twob2v4 = data['b2v4']
                user.machine_time.twob2v5 = data['b2v5']
                user.machine_time.twob2v6 = data['b2v6']

                user.machine_time.threeb3v1 = data['b3v1']
                user.machine_time.threeb3v2 = data['b3v2']
                user.machine_time.threeb3v3 = data['b3v3']
                user.machine_time.threeb3v4 = data['b3v4']
                user.machine_time.threeb3v5 = data['b3v5']
                user.machine_time.threeb3v6 = data['b3v6']
                print("dsa")
                user.machine_time.save()
            else:
                mdata = {
                        'onetime': data['b1t'],
                        'twotime': data['b2t'],
                        'threetime': data['b3t'],
                        'oneb1v1': data['b1v1'],
                        'oneb1v2': data['b1v2'],
                        'oneb1v3': data['b1v3'],
                        'oneb1v4': data['b1v4'],
                        'oneb1v5': data['b1v5'],
                        'oneb1v6': data['b1v6'],
                        'twob2v1': data['b2v1'],
                        'twob2v2': data['b2v2'],
                        'twob2v3': data['b2v3'],
                        'twob2v4': data['b2v4'],
                        'twob2v5': data['b2v5'],
                        'twob2v6': data['b2v6'],
                        'threeb3v1': data['b3v1'],
                        'threeb3v2': data['b3v2'],
                        'threeb3v3': data['b3v3'],
                        'threeb3v4': data['b3v4'],
                        'threeb3v5': data['b3v5'],
                        'threeb3v6': data['b3v6'],

                }
                machine = MachineTime.objects.create(**mdata)
                user.machine_time = machine
                user.save()
        return restful.ok()

@csrf_exempt
def box_get(request):
    if request.method == "POST":
        lon = request.POST.get("lon")
        lat = request.POST.get("lat")
        is_fall = request.POST.get("fall")
        is_call = request.POST.get("call")
        uid = request.POST.get("machine_id")
        print(uid)
        print(request.body)
        if not uid:
            msg = eval(request.body)
            lon = msg['lon']
            lat = msg['lat']
            is_fall = msg['fall']
            is_call = msg['call']
            uid = msg['machine_id']
        user = User.objects.get(machineId=uid)
        if is_call == '1':
            call = True
        else:
            call = False
        if is_fall == '1':
            fall = True
        else:
            fall = False
        txt = ""
        if user:
            print(user)
            user.x = lon
            user.y = lat
            user.is_call =call
            user.is_fall =fall
            onetime = user.machine_time.onetime
            twotime = user.machine_time.twotime
            threetime = user.machine_time.threetime
            onetime = onetime.replace(':',"") + "00"
            twotime = twotime.replace(':',"") + "00"
            threetime = threetime.replace(':',"") + "00"
            b1v1 = str(user.machine_time.oneb1v1)
            b1v2 = str(user.machine_time.oneb1v2)
            b1v3 = str(user.machine_time.oneb1v3)
            b1v4 = str(user.machine_time.oneb1v4)
            b1v5 = str(user.machine_time.oneb1v5)
            b1v6 = str(user.machine_time.oneb1v6)
            b2v1 = str(user.machine_time.twob2v1)
            b2v2 = str(user.machine_time.twob2v2)
            b2v3 = str(user.machine_time.twob2v3)
            b2v4 = str(user.machine_time.twob2v4)
            b2v5 = str(user.machine_time.twob2v5)
            b2v6 = str(user.machine_time.twob2v6)
            b3v1 = str(user.machine_time.threeb3v1)
            b3v2 = str(user.machine_time.threeb3v2)
            b3v3 = str(user.machine_time.threeb3v3)
            b3v4 = str(user.machine_time.threeb3v4)
            b3v5 = str(user.machine_time.threeb3v5)
            b3v6 = str(user.machine_time.threeb3v6)
            txt += onetime + twotime + threetime + b1v1 + b1v2 + b1v3 +b1v4 + b1v5+b1v6+b2v1+ b2v2 + b2v3 +b2v4 + b2v5+b2v6+ b3v1 + b3v2 + b3v3 +b3v4 + b3v5+b3v6+user.harry_telephone
            user.save()
            return HttpResponse(txt)
        else:
            return restful.params_error()
    else:
        user = User.objects.get(uid=1)
        txt = ""
        if user:
            onetime = user.machine_time.onetime
            twotime = user.machine_time.twotime
            threetime = user.machine_time.threetime
            onetime = onetime.replace(':',"") + "00"
            twotime = twotime.replace(':',"") + "00"
            threetime = threetime.replace(':',"") + "00"
            b1v1 = str(user.machine_time.oneb1v1)
            b1v2 = str(user.machine_time.oneb1v2)
            b1v3 = str(user.machine_time.oneb1v3)
            b1v4 = str(user.machine_time.oneb1v4)
            b1v5 = str(user.machine_time.oneb1v5)
            b1v6 = str(user.machine_time.oneb1v6)
            b2v1 = str(user.machine_time.twob2v1)
            b2v2 = str(user.machine_time.twob2v2)
            b2v3 = str(user.machine_time.twob2v3)
            b2v4 = str(user.machine_time.twob2v4)
            b2v5 = str(user.machine_time.twob2v5)
            b2v6 = str(user.machine_time.twob2v6)
            b3v1 = str(user.machine_time.threeb3v1)
            b3v2 = str(user.machine_time.threeb3v2)
            b3v3 = str(user.machine_time.threeb3v3)
            b3v4 = str(user.machine_time.threeb3v4)
            b3v5 = str(user.machine_time.threeb3v5)
            b3v6 = str(user.machine_time.threeb3v6)
            txt += onetime + twotime + threetime + b1v1 + b1v2 + b1v3 +b1v4 + b1v5+b1v6+b2v1+ b2v2 + b2v3 +b2v4 + b2v5+b2v6+ b3v1 + b3v2 + b3v3 +b3v4 + b3v5+b3v6+user.harry_telephone
            return HttpResponse(txt)
        else:
            return restful.params_error()

def set_telephone(request):
    id = request.POST.get('uid')
    telephone = request.POST.get('telephone')
    user = User.objects.get(uid=id)
    if user:
        user.harry_telephone = telephone
        user.save()
        return  restful.ok()
    else:
        return restful.unauth()

def detail(request,id):
    try:
        news = News.objects.get(id=id)
        context = {'news':news}
        return render(request,'read_more.html',context=context)
    except Exception as e:
        print(e)
        raise Http404()

def comment(request):
    id = request.POST.get('id')
    comment = request.POST.get('comment')
    print(id)
    print(comment)
    comments = CommentNews.objects.create(content=comment,author_id=request.user.uid,news_id=id)
    serizlize = CommentSerizlizer(comments)
    print(serizlize.data)
    return restful.ok(data=serizlize.data)