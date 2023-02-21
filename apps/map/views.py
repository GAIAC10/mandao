from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Machine
# Create your views here.
import requests
from utils import restful

# url = r'https://tsapi.amap.com/v1/track/service/add'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
# }
# data = {
#     'key': 'a160cfadd311717658e2a3ed0c64cedf',
#     'name': 'usermap',
#     'desc': "usermap"
# }
#
# res = requests.post(url,header,data)
# print(res.text)
@login_required
def map_index(request):
    return render(request,'map.html')


def search_x_y(request):
    x = request.user.x
    y = request.user.y
    data = {
        'x': x,
        'y': y,
    }
    return restful.ok(data=data)