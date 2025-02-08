from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('tapdoan/', views.tapdoan, name='tapdoan'),
    path('lichsu/', views.lichsu, name='lichsu'),
    path('hethongfpt/', views.hethongfpt, name='hethongfpt'),
    path('chuongtrinhdaotao/', views.chuongtrinhdaotao, name='chuongtrinhdaotao'),
    path('congcuhoctap/', views.congcuhoctap, name='congcuhoctap'),
    path('monhoc/', views.monhoc, name='monhoc'),
    path('lienhe/', views.lienhe, name='lienhe'),
    path('diendan/', views.diendan, name='diendan'),
    path('dangnhap/', views.dangnhap, name='dangnhap'),
    path('dangky/', views.dangky, name='dangky'),

]