from django.urls import path
from book.views import index

urlpatterns = [

    #添加一条路由匹配
    #格式  path('路由’，视图函数名）
    path('index/', index),
]