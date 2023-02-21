from django.db import models

# Create your models here.
class MdImg(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='media')
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100,blank=True)
    youxian = models.CharField(max_length=100,blank=True,default=1)
    link = models.URLField(max_length=100,blank=True,default="http://127.0.0.1:8000")

class News(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateField(auto_now_add=True)
    comments_counts = models.IntegerField()
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.URLField(default='http://imgs.bootstrapmb.com/2020/7/210855189s.jpg')
    author = models.ForeignKey('mdauth.User',on_delete=models.CASCADE,related_name='author')

    class Meta:
        ordering = ['-time']

class CommentNews(models.Model):
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey("News",on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey("mdauth.User",on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_time']

class MachineTime(models.Model):
    id = models.AutoField(primary_key=True)
    onetime = models.CharField(max_length=20)
    twotime = models.CharField(max_length=20)
    threetime = models.CharField(max_length=20)
    oneb1v1 = models.IntegerField(default=0)
    oneb1v2 = models.IntegerField(default=0)
    oneb1v3 = models.IntegerField(default=0)
    oneb1v4 = models.IntegerField(default=0)
    oneb1v5 = models.IntegerField(default=0)
    oneb1v6 = models.IntegerField(default=0)
    twob2v1 = models.IntegerField(default=0)
    twob2v2 = models.IntegerField(default=0)
    twob2v3 = models.IntegerField(default=0)
    twob2v4 = models.IntegerField(default=0)
    twob2v5 = models.IntegerField(default=0)
    twob2v6 = models.IntegerField(default=0)
    threeb3v1 = models.IntegerField(default=0)
    threeb3v2 = models.IntegerField(default=0)
    threeb3v3 = models.IntegerField(default=0)
    threeb3v4 = models.IntegerField(default=0)
    threeb3v5 = models.IntegerField(default=0)
    threeb3v6 = models.IntegerField(default=0)
