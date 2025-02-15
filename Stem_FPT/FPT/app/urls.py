from django.contrib import admin
from django.urls import path, include
from . import views
from .views import search_view
from django.contrib.auth.views import LogoutView
from .views import post_detail
from django.contrib import admin


urlpatterns = [
    path('', views.home, name ='home'),
    path('home1/', views.home1, name='home1'),
    path('home2/', views.home2, name='home2'),
    path('home3/', views.home3, name='home3'),
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
    path("dangxuat/", views.dangxuat, name="dangxuat"),
    path('dangky/', views.dangky, name='dangky'),
    path('thongtinsinhvien/', views.thongtinsinhvien, name='thongtinsinhvien'),
    path('themanhdaotao/', views.themanhdaotao, name='themanhdaotao'),
    path('tuyensinh/', views.tuyensinh, name='tuyensinh'),
    path('hocphi', views.hocphi, name='hocphi'),
    path('khoiphucmatkhau', views.khoiphucmatkhau, name='khoiphucmatkhau'),
    path('bot', views.bot, name='bot'),
    path('thaoluankhoahoc', views.thaoluankhoahoc, name='thaoluankhoahoc'),
    path('xuhuongcn', views.xuhuongcn, name='xuhuongcn'),
    path('chitietkythuat', views.chitietkythuat, name='chitietkythuat'),
    path('toanhoc', views.toanhoc, name='toanhoc'),
    path('nlmt', views.nlmt, name='nlmt'),
    path('robotdk', views.robotdk, name='robotdk'),
    path('maylocnuoc', views.maylocnuoc, name='maylocnuoc'),
    path('chinhsuathongtin/', views.chinhsuathongtin, name='chinhsuathongtin'),
    path('dangky_success/', views.dangky_success, name='dangky_success'),
    path('search/', search_view, name='search'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('doimatkhau/', views.doimatkhau, name='doimatkhau'),
]