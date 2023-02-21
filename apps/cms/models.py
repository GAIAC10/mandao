from django.db import models
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    addr = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)
    qq = models.CharField(max_length=12)
    kefu = models.CharField(max_length=20)
    Email = models.EmailField()
    wechat = models.URLField()

class Vip(models.Model):
    money = models.CharField(max_length=100,default=0)

class Comment(models.Model):
    is_read = models.BooleanField(default=0)
    content = models.CharField(max_length=500)
    last_login = models.DateField(auto_now=True)






