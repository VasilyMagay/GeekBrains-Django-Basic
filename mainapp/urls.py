from django.contrib import admin
from django.urls import path, re_path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.index, name='index'),
    re_path(r'^products/$', mainapp.products, name='products'),
    re_path(r'^contact/$', mainapp.contact, name='contact'),

    re_path(r'^catalog/category/(\d+)/$', mainapp.products, name='catalog'),
    re_path(r'^catalog/category/(?P<category_pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='catalog'),

    # ?P<pk> - именованный параметр
    re_path(r'^catalog/product/(?P<pk>\d+)/$', mainapp.product, name='product'),
]
