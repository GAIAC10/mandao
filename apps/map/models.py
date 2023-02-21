from django.db import models

# Create your models here.

class Machine(models.Model):
    x = models.CharField(max_length=100)
    y = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11,unique=True)
    sid = models.CharField(max_length=100,primary_key=True,unique=True)

    def __str__(self):
        return self.sid
    class Meta:
        db_table = "machine"
        # 定义在管理后台显示的名称
        verbose_name = '设备'
        # 定义复数时的名称（去除复数的s）
        verbose_name_plural = verbose_name


