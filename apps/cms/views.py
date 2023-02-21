import os

from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.http import FileResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from apps.cms.models import Comment
from apps.mdauth.models import User
from apps.mdmain.models import MdImg
from .forms import BannerForm, wechatEcodeForm, Person, CreatAdminForm
from . models import Company
from utils import restful
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
# from utils import sms
from ..mdauth.decrators import cc_staff_required,cc_superuser_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
logger = logging.getLogger('log')

def _get_page(object_list, per_page,p,end_count=1):
    paginator = Paginator(object_list,per_page,end_count)
    contacts = paginator.page(p)
    return  paginator,contacts

@cc_staff_required
def cms_index(request):

    logger.info('请求成功！ 用户:{}进入猿泓cms管理后台！；response_headers:{}；request_body:{},'.format(request.user, request.headers,
                                                                                     request.body[:251]))
    return render(request, 'cms/cms_index.html')
@cc_staff_required
def controlpanel(request):
    user = User.objects.filter().all()
    p = int(request.GET.get("p",1))
    pagination,contacts = _get_page(user,10,p)
    context_data = get_pagination_data(pagination,contacts)
    context = {
        'contacts': contacts
    }
    context.update(context_data)

    return render(request, 'cms/controlpanel.html',context=context)
@cc_staff_required
def banners(request):
    imgs = MdImg.objects.filter().order_by('youxian')
    p = int(request.GET.get("p", 1))
    paginator, contacts = _get_page(imgs, 10, p)
    context_data = get_pagination_data(paginator,contacts)
    context = {
        "contacts":contacts
    }
    print(contacts.start_index)
    context.update(context_data)
    print(context)
    return render(request, 'cms/banners.html',context=context)

def get_pagination_data(paginator,contacts,around_counts = 2):
    current_page = contacts.number
    nums_pages = paginator.num_pages
    left_has_more = False
    right_has_more = False
    if current_page <= around_counts + 2:
        left_pages = range(1,current_page)
    else:
        left_has_more = True
        left_pages = range(current_page - around_counts,current_page)
    if current_page >= nums_pages - around_counts - 1:
        right_pages = range(current_page + 1, nums_pages+1)
    else:
        right_has_more = True
        right_pages = range(current_page+1, current_page + around_counts+1 )
    print(left_pages)
    print(right_pages)
    return {
        'left_pages': left_pages,
        # right_pages：代表的是当前这页的右边的页的页码
        'right_pages': right_pages,
        'current_page': current_page,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'nums_pages': nums_pages
    }



@cc_staff_required
def picture_create(request):
    return render(request, 'cms/picture_create.html')

@method_decorator(cc_superuser_required,name="dispatch")

class webset(View):
    def get(self,request):
        return render(request, 'cms/webset.html')
    def post(self,request):

        return restful.ok()

@method_decorator(cc_staff_required,name="dispatch")
class administrators(View):
    def get(self,request):
        users = User.objects.all()
        p = int(request.GET.get("p", 1))
        paginator, contacts = _get_page(users, 10, p)
        context_data = get_pagination_data(paginator, contacts)
        context = {
            'contacts': contacts
        }
        context.update(context_data)
        return render(request, 'cms/administrators.html',context=context)
    def post(self,request):
        form = Person(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            uid = form.cleaned_data.get('uid')
            telephone = form.cleaned_data.get('telephone')
            user = User.objects.get(uid=uid)
            user.username = username
            user.set_password(password)
            user.telephone = telephone
            user.save()
            logger.info("请求成功！ 用户:{}将{}的账户密码！将{}:{}修改为{}:{}".format(request.user,user.telephone,telephone,
                                                                       password,user.telephone,user.password))
            return restful.ok()

def persons(request):
    users = User.objects.filter(is_superuser__exact=0).order_by('-is_vip')
    p = int(request.GET.get("p", 1))
    paginator, contacts = _get_page(users, 10, p)
    context_data = get_pagination_data(paginator,contacts)
    context = {
        'contacts': contacts
    }
    context.update(context_data)

    return render(request,'cms/persons.html',context=context)


@method_decorator(cc_staff_required,name="dispatch")
class user(View):
    def get(self,request):
        users = User.objects.filter(is_vip=1)
        pagination = Paginator(users, 1, 1)
        p = int(request.GET.get('p', 1))
        contacts = pagination.page(p)
        context_data = get_pagination_data(pagination, contacts)
        context = {
            'contacts': contacts
        }
        context.update(context_data)
        return render(request, 'cms/user.html',context=context)
    def post(self,request):
        logger = logging.getLogger('log')
        password = request.POST.get("password")
        uid = request.POST.get("uid")
        print(uid)
        user = User.objects.get(uid=uid)
        if user:
            user.password =  make_password(password,"a",'pbkdf2_sha1')
            logger.info("请求成功！ 用户:{}将{}的账户密码！将{}:{}修改为{}:{}".format(request.user, user.telephone, user.telephone,
                                                                    user.password, user.telephone, password))
            user.save()
            return restful.ok()
        else:
            return restful.params_error("刷新后重试！！！")

@cc_superuser_required
def logs(request):
    downloads_lists = os.listdir(os.path.join(settings.BASE_DIR,'logs'))
    pagination = Paginator(downloads_lists,5,1)
    p = int(request.GET.get('p',1))
    contacts = pagination.page(p)
    context_data = get_pagination_data(pagination,contacts)

    context = {
        'contacts':contacts
    }
    context.update(context_data)
    # with open(os.path.join(settings.BASE_DIR, 'logs')) as fp:
    #     pass
    return render(request, 'cms/logs.html',context=context)

def download_logs(request,filename):
    f = open(os.path.join(settings.BASE_DIR,'logs',filename), 'rb')
    response = FileResponse(f)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response




@cc_staff_required
def message(request):
    comments = Comment.objects.all().order_by('comment__is_vip')
    p = int(request.GET.get("p", 1))
    paginator, contacts = _get_page(comments, 10, p)
    context_data = get_pagination_data(paginator,contacts)
    context = {
        'contacts': contacts,
    }
    context.update(context_data)
    return render(request, 'cms/message.html',context=context)

@cc_staff_required
def turn_black(request):

    id = request.POST.get("id")
    user = User.objects.get(uid=id)
    if user:
        user.is_active = False
        user.save()
        logger.warning("请求成功！ 用户:{}将{}的账户拉黑了！".format(request.user, user.telephone))
        return restful.ok()
    else:
        return restful.params_error('请刷新后重试！')
@cc_superuser_required
def delete(request):

    id = request.POST.get("id")
    user = User.objects.get(uid=id)
    if user:
        user.delete()
        logger.warning("请求成功！ 用户:{}将{}的账户删除了！".format(request.user, user.telephone))
        return restful.ok()
    else:
        return restful.params_error('请刷新后重试！')
@cc_staff_required
def edit_banner(request):
    form = BannerForm(request.POST)
    if form.is_valid():
        desc = form.cleaned_data.get("desc")
        name = form.cleaned_data.get("name")
        link = form.cleaned_data.get("link")
        id = form.cleaned_data.get("id")
        youxian = form.cleaned_data.get("youxian")
        banner = MdImg.objects.get(id=id)
        if banner:
            banner.link = link
            banner.desc = desc
            banner.name = name
            banner.youxian = youxian
            banner.save()
            logger.info('用户:{} 修改了轮播图的详细内容！'.format(request.user))
            return restful.ok()
        else:
            return restful.unauth()
    else:

        return restful.params_error(form.get_errors())

@cc_staff_required
def upload(request):
    file = request.FILES.get('file')
    with open(os.path.join(settings.MEDIA_ROOT,'wechat',file.name), 'wb') as f:
        for i in file:
            f.write(i)
    url = request.build_absolute_uri(settings.MEDIA_URL + file.name)
    logger.info("用户{}上传了{}文件到猿泓".format(request.user, file.name))
    return restful.ok(data=url)
@cc_staff_required
def wechatEcode(request):
    form = wechatEcodeForm(request.POST)
    if form.is_valid():
        img = form.cleaned_data.get('wechat')
        name = form.cleaned_data.get('name')
        addr = form.cleaned_data.get('addr')
        telephone = form.cleaned_data.get('telephone')
        qq = form.cleaned_data.get('qq')
        kefu = form.cleaned_data.get('kefu')
        Email = form.cleaned_data.get('Email')
        company = Company.objects.all()
        if company:
            com = company.get()
            com.wechat = img
            com.name = name
            com.addr = addr
            com.telephone = telephone
            com.qq = qq
            com.kefu = kefu
            com.Email = Email
            com.save()
        else:
            com = Company.objects.create(wechat=img,name=name,addr=addr,telephone=telephone,qq=qq,kefu=kefu,Email=Email)
            com.save()
            logger.warning("用户{}更新了网站的基本信息！".format(request.user))
        return restful.ok()
    else:
        print(form.errors)
        logger.error("请求失败！原因：{}".format(form.errors))
        return restful.params_error(message=form.get_errors())

@cc_staff_required
def send_sms(request):
    uid  = request.POST.get('uid')
    password  = request.POST.get('password')
    try:
        user = User.objects.get(uid=uid)
        name = user.username
        phone = user.telephone
        if(sms.Sample.main(phone,{"name": name,'password': password})):
            return restful.ok()
        else:
            return restful.params_error("账户余额不足或者没有权限！")
    except:
        return restful.params_error("没有这个人！")

class CreatAdmin(View):
    def get(self,request):
        groups = Group.objects.all()
        context = {
            'groups':groups
        }
        return render(request,'cms/creat_administrators.html',context=context)
    def post(self,request):
        form = CreatAdminForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            select = form.cleaned_data.get('select')
            print(select)

            try:
                user = User.objects.get(telephone=telephone)
                print(user)
                user.is_staff = True
                _groups = Group.objects.filter(pk=select)
                print(_groups)
                user.groups.set(_groups)
                user.is_superuser = "1"
                user.save()
                logger.info("用户{}修改了一位职员的权限{}，修改为{}".format(request.user, user.telephone,user.groups.get().name))
                return restful.ok()
            except:
                user = User.objects.create(username=username,telephone=telephone,password=password)
                user.is_staff = True
                groups = Group.objects.filter(pk=select)
                user.groups.set(groups)
                user.save()
                logger.info("用户{}添加了一位新职员{},职位是{}".format(request.user, user.telephone,user.groups.name))
                return restful.ok()
        else:
            print(form.errors)
            return restful.params_error("参数错误！")

@cc_staff_required
class news(View):
    def get(self,request):
        return render(request,'cms/news.html')

    def post(self,request):
        pass