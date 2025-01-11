from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def courses(request):
    return render(request, 'home/courses.html')

def contact(request):
    return render(request, 'home/contact.html')

def tapdoan(request):
    return render(request, 'home/tapdoan.html')

def lichsu(request):
    return render(request, 'home/lichsu.html')

def thongbao(request):
    return render(request, 'home/thongbao.html')

