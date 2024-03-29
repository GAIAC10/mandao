# Generated by Django 3.2.4 on 2021-09-12 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('onetime', models.CharField(max_length=20)),
                ('twotime', models.CharField(max_length=20)),
                ('threetime', models.CharField(max_length=20)),
                ('oneb1v1', models.IntegerField(default=0)),
                ('oneb1v2', models.IntegerField(default=0)),
                ('oneb1v3', models.IntegerField(default=0)),
                ('oneb1v4', models.IntegerField(default=0)),
                ('oneb1v5', models.IntegerField(default=0)),
                ('oneb1v6', models.IntegerField(default=0)),
                ('twob2v1', models.IntegerField(default=0)),
                ('twob2v2', models.IntegerField(default=0)),
                ('twob2v3', models.IntegerField(default=0)),
                ('twob2v4', models.IntegerField(default=0)),
                ('twob2v5', models.IntegerField(default=0)),
                ('twob2v6', models.IntegerField(default=0)),
                ('threeb3v1', models.IntegerField(default=0)),
                ('threeb3v2', models.IntegerField(default=0)),
                ('threeb3v3', models.IntegerField(default=0)),
                ('threeb3v4', models.IntegerField(default=0)),
                ('threeb3v5', models.IntegerField(default=0)),
                ('threeb3v6', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MdImg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=100)),
                ('youxian', models.CharField(blank=True, default=1, max_length=100)),
                ('link', models.URLField(blank=True, default='http://127.0.0.1:8000', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateField(auto_now_add=True)),
                ('comments_counts', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('thumbnail', models.URLField(default='http://imgs.bootstrapmb.com/2020/7/210855189s.jpg')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='CommentNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mdmain.news')),
            ],
            options={
                'ordering': ['-pub_time'],
            },
        ),
    ]
