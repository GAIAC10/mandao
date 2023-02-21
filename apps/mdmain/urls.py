from django.urls import path
from . import views

app_name= "mdmain"

urlpatterns = [
    path("upload/",views.upload,name="upload"),
    path("add_banners/",views.add_banners,name="add_banners"),
    path("contact/",views.contact.as_view(),name="contact"),
    path("works/",views.works,name="works"),
    path("work_detail/",views.work_detail,name="work_detail"),
    path("choose/",views.choose.as_view(),name="choose"),
    path("box_get/",views.box_get,name="box_get"),
    path("set_telephone/",views.set_telephone,name="set_telephone"),
    path("detail/<int:id>/",views.detail,name="detail"),
    path("comment/",views.comment,name="comment"),
]