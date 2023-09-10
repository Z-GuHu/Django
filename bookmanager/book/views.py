from django.shortcuts import render
from book.models import BookInfo, PeopleInfo

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    #render 渲染模板
    #def render(request, template_name, context=None, content_type=None, status=None, using=None):
    books = BookInfo.objects.all()
    context = {
        'name': "asd"
    }
    return render(request, 'book/index.html', context=context)


