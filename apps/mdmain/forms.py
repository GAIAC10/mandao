from django import forms
from utils.restful import FormMixin

class Img(forms.Form,FormMixin):
    img = forms.URLField()
    banner_desc = forms.CharField(max_length=100)
    link = forms.URLField()
    youxian = forms.IntegerField()
    name = forms.CharField(max_length=100)

class ContactForm(forms.Form,FormMixin):
    username = forms.CharField(max_length=30)
    telephone = forms.CharField(max_length=11)
    content = forms.CharField(widget=forms.Textarea)
