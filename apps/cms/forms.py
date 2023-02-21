from django import forms
from django.forms import ModelForm
from . import models
from ..mdauth.models import User
from ..mdmain.models import News


class FormMixin(object):
    def get_errors(self):
        if hasattr(self, 'errors'):
            errors = self.errors.get_json_data()
            new_errors = {}
            for key, message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}


class BannerForm(forms.Form,FormMixin):
    desc = forms.CharField(max_length=100)
    id = forms.IntegerField()
    link = forms.URLField()
    youxian = forms.IntegerField()
    name = forms.CharField(max_length=50)


class wechatEcodeForm(ModelForm, FormMixin):
    class Meta:
        model= models.Company
        fields = '__all__'


class NewsForm(ModelForm, FormMixin):
    class Meta:
        model= News
        fields = '__all__'

class Person(ModelForm):
    password = forms.CharField(max_length=100)
    uid = forms.IntegerField()
    class Meta:
        model=User
        fields = ('telephone','username',)


class CreatAdminForm(forms.Form):
    password = forms.CharField(max_length=100)
    select = forms.IntegerField()
    telephone = forms.CharField(max_length=11)
    username = forms.CharField(max_length=100)
