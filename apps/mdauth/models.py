from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from shortuuidfield import ShortUUIDField

from apps.cms.models import Vip, Comment
from apps.mdmain.models import MachineTime

SEX = (("男","男"),("女","女"))

class UserManager(BaseUserManager):
    def _create_user(self,telephone, username,password,**kwargs):
        if not telephone:
            raise ValueError('请传入手机号码！')
        if not username:
            raise ValueError('请传入用户名！')
        if not password:
            raise ValueError('请传入密码！')

        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    # 下面这两个函数在createsuperuser和创建用户的时候调用(在函数里加入一些必填的字段)
    # 创建用户
    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone, username, password, **kwargs)

    # 创建超级用户
    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone, username, password, **kwargs)

class User(AbstractBaseUser,PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    telephone = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_vip = models.BooleanField(default=0)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)
    sex = models.CharField('性别', max_length=4, choices=SEX, default='男')
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='最后登录时间')
    is_fall = models.BooleanField(default=False)
    is_call = models.BooleanField(default=False)
    harry_telephone = models.CharField(max_length=11,blank=True)
    flag = models.BooleanField(default=0)
    x = models.CharField(max_length=100,blank=True)
    y = models.CharField(max_length=100,blank=True)
    money = models.ForeignKey(Vip,on_delete=models.CASCADE,related_name='user_money',null=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name='comment',null=True)
    machine_time = models.ForeignKey(MachineTime,on_delete=models.CASCADE,related_name='time',null=True)
    machineId = models.TextField(max_length=100,blank=True,default=00000000000)

    # telephone，username，password

    # 将'xxx'作为用户名(默认是username)
    USERNAME_FIELD = 'telephone'
    # 必填字段
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.telephone