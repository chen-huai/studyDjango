from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    test          = {}
    test['hello'] = 'Hello test!'
    views_name = "菜鸟教程"
    return render(request, 'runoob.html', {"name": views_name})
