from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    book = models.Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    book.save()
    return HttpResponse("<p>数据添加成功！</p>")
def search_book(request):
    books = models.Book.objects.filter(pk=1)
    res = ''
    print(111,books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    for each in books:
        res += each.title
    print(res)
    return HttpResponse("<p>查找成功！</p>%s" % res)
def exclude_book(request):
    # exclude() 方法用于查询不符合条件的数据。
    books = models.Book.objects.exclude(pk=2)
    res = ''
    print(books)
    print("//////////////////////////////////////")
    books = models.Book.objects.exclude(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    for each in books:
        res += each.title
    print(res)
    return HttpResponse("<p>查找成功！</p>%s" % res)
def reverse_book(request):
    # 按照价格升序排列：降序再反转
    res = ''
    books = models.Book.objects.order_by("price").reverse()
    for each in books:
        res += str(each.pk)
    return HttpResponse("<p>查找成功！</p>%s"%res)