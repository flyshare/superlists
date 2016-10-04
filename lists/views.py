from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    """
    Django 的 render()函数,1:请求对象 2:渲染的模板名
    render()会在所有的应用目录中搜索名为 templates 的文件夹
    然后根据模板中的内容构建一个 HttpResponse对象
    render() 比 Python原生的open()强大的多
    """
    return render(request, 'home.html', {'new_item_text': '1. Buy peacock feathers'})
