from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context= {}
    return render(request, 'app/home.html',context)
def tapdoan(request):
    context= {}
    return render(request, 'app/tapdoan.html',context)
def lichsu(request):
    context= {}
    return render(request, 'app/lichsu.html',context)

def hethongfpt(request):
    context= {}
    return render(request, 'app/hethongfpt.html',context)

def chuongtrinhdaotao(request):
    context= {}
    return render(request, 'app/chuongtrinhdaotao.html',context)

def congcuhoctap(request):
    context= {}
    return render(request, 'app/congcuhoctap.html',context)

def monhoc(request):
    context= {}
    return render(request, 'app/monhoc.html',context)

def lienhe(request):
    context= {}
    return render(request, 'app/lienhe.html',context)