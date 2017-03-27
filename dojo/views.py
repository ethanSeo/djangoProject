from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os

def mysum(request, numbers):
    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)
def hello(request, name, age):
    return HttpResponse('안녕하세요, {}! {}살이시네요.'.format(name, age))

def post_list1(request):
    name = 'Ethan'
    return HttpResponse('''
    <h1>Ask Django</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&자고 페이스메이커</p>
    '''.format(name=name))

def post_list2(request):
    name = 'Ethan'
    return render(request, 'dojo/post_list.html', {'name': name})

def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
    #filepath = '/Users/ethanseo/anaconda/pkgs/pandas-0.18.1-np111py35_0/lib/python3.5/site-packages/pandas/io/tests/data/times_1900.xls'
    filepath = os.path.join(settings.BASE_DIR, 'times_1900.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type= 'application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
