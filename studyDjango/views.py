from django.http import HttpResponse
from django.shortcuts import render,redirect



def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    test          = {}
    test['hello'] = 'Hello test!'
    views_name = "菜鸟教程"
    return render(request, 'runoob.html', {"name": views_name})
def img(request):
    name ="菜鸟教程"
    return render(request, "runoob.html", {"name": name})
def baby(request):
    name ="菜鸟教程"
    return render(request, "baby.html", {"name": name})

def getMethod(request):
    name = request.GET.get("name")
    return HttpResponse('姓名：{}'.format(name))
def postMethod(request):
    name = request.POST.get("name")
    return HttpResponse('姓名：{}'.format(name))
def bodyMethod(request):
    name = request.body
    print(name)
    return HttpResponse("body")
def pathMethod(request):
    name = request.path
    print(name)
    return HttpResponse("path")
def httpRes(request):
    # return HttpResponse("菜鸟教程")
    # HttpResponse(): 返回文本，参数为字符串，字符串中写文本内容。如果参数为字符串里含有 html 标签，也可以渲染
    return HttpResponse("<a href='https://www.runoob.com/'>菜鸟教程</a>")
def renderMethod(request):
    # render(): 返回文本，第一个参数为 request，第二个参数为字符串（页面名称），第三个参数为字典（可选参数，向页面传递的参数：键为页面参数名，值为views参数名）。
    name = "菜鸟教程"
    hello = 'hello'
    # return render(request,"runoob.html",{"name":name})
    return render(request,"runoob.html",{"name":name,"hello":hello})
def redirectMethod(request):
    # redirect()：重定向，跳转新页面。参数为字符串，字符串中填写页面路径。一般用于form表单提交后，跳转到新页面。
    return redirect("https://www.baidu.com")
    # return render(request,"/")