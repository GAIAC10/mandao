from django.urls import path
from . import views


app_name = 'cms'

urlpatterns = [

    path("",views.cms_index, name='cms_index'),
    path("controlpanel/",views.controlpanel, name='controlpanel'),
    path("banners/",views.banners, name='banners'),
    path("picture_create/",views.picture_create, name='picture_create'),
    path("webset/",views.webset.as_view(), name='webset'),
    path("administrators/",views.administrators.as_view(), name='administrators'),
    path("user/",views.user.as_view(), name='user'),
    path("logs/",views.logs, name='logs'),
    path("message/",views.message, name='message'),
    path("turn_black/",views.turn_black, name='turn_black'),
    path("delete/",views.delete, name='delete'),
    path("edit_banner/",views.edit_banner, name='edit_banner'),
    path("upload/",views.upload, name='upload'),
    path("wechatEcode/",views.wechatEcode, name='wechatEcode'),
    path("send_sms/",views.send_sms, name='send_sms'),
    path("creat_admin/",views.CreatAdmin.as_view(), name='creat_admin'),
    path("download_logs/<str:filename>",views.download_logs, name='download_logs'),
    path("persons/",views.persons, name='persons'),
]