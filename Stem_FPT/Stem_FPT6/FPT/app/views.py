from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from app.models import Profile
from .models import SinhVien  
from .forms import SinhVienForm  
from .forms import ProfileForm
from .models import LienHe
from .models import DangKy
from .forms import FormDangKy
from .models import Post  
import unicodedata

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
    if request.method == "POST":
        ho_ten = request.POST.get('name')
        email = request.POST.get('email')
        loi_nhan = request.POST.get('message')

        # Lưu vào database
        LienHe.objects.create(ho_ten=ho_ten, email=email, loi_nhan=loi_nhan)

        # Hiển thị thông báo thành công
        messages.success(request, "Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi sớm nhất.")

        return redirect('lienhe')  # Quay lại trang liên hệ sau khi gửi

    return render(request, 'app/lienhe.html')

def diendan(request):
    context= {}
    return render(request, 'app/diendan.html',context)

def dangnhap(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect after successful login
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không chính xác!")
    
    return render(request, 'app/dangnhap.html')

def dangxuat(request):
    logout(request)
    return redirect("dangnhap")


def dangky(request):
    if request.method == 'POST':
        form = FormDangKy(request.POST)
        if form.is_valid():
            form.save()  # Lưu thông tin vào cơ sở dữ liệu
            return redirect('dangky_success')  # Chuyển hướng đến trang thành công
    else:
        form = FormDangKy()  # Nếu chưa gửi form thì tạo form mới

    return render(request, 'app/dangky.html', {'form': form})


def themanhdaotao(request):
    context= {}
    return render(request, 'app/themanhdaotao.html',context)

def tuyensinh(request):
    context= {}
    return render(request, 'app/tuyensinh.html',context)

def hocphi(request):
    context= {}
    return render(request, 'app/hocphi.html',context)

def khoiphucmatkhau(request):
    context={}
    return render(request, 'app/khoiphucmatkhau.html',context)

def bot(request):
    context={}
    return render(request, 'app/bot.html',context)

def thaoluankhoahoc(request):
    context={}
    return render(request, 'app/thaoluankhoahoc.html',context)

def xuhuongcn(request):
    context={}
    return render(request, 'app/xuhuongcn.html',context)

def chitietkythuat(request):
    context={}
    return render(request, 'app/chitietkythuat.html',context)

def toanhoc(request):
    context={}
    return render(request, 'app/toanhoc.html',context)

def nlmt(request):
    context={}
    return render(request, 'app/nlmt.html',context)

def robotdk(request):
    context={}
    return render(request, 'app/robotdk.html', context)

def maylocnuoc(request):
    context={}
    return render(request, 'app/maylocnuoc.html', context)

def thongtinsinhvien(request):
    user = request.user
    if user.is_authenticated:
        profile, created = Profile.objects.get_or_create(user=user)  # Tạo Profile nếu chưa có
        student_info = {
            'name': f"{user.first_name} {user.last_name}",
            'mssv': profile.mssv or '',
            'class_name': profile.class_name or '',
            'nam_hoc': profile.nam_hoc or '',
            'nam_sinh': profile.nam_sinh or '',
            'dia_chi_thuong_tru': profile.dia_chi_thuong_tru or '',
            'que_quan': profile.que_quan or '',
            'so_dien_thoai': profile.so_dien_thoai or '',
            'email': user.email,
            'thong_tin_gia_dinh': profile.thong_tin_gia_dinh or '',
        }
    else:
        student_info = {key: '' for key in ['name', 'mssv', 'class_name', 'nam_hoc', 'nam_sinh', 'dia_chi_thuong_tru', 'que_quan', 'so_dien_thoai', 'email', 'thong_tin_gia_dinh']}

    return render(request, 'app/thongtinsinhvien.html', {'student_info': student_info})

def chinhsuathongtin(request):
    profile = Profile.objects.get(user=request.user)  # Lấy Profile của người dùng hiện tại
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('thongtinsinhvien')  # Chuyển hướng về trang thongtinsinhvien sau khi lưu
    else:
        form = ProfileForm(instance=profile)  # Nếu GET, hiển thị form với thông tin hiện tại

    return render(request, 'app/chinhsuathongtin.html', {'form': form})

def dangky_success(request):
    return render(request, 'app/dangky_success.html')


def remove_accents(input_str):
    """Chuyển đổi chuỗi có dấu thành không dấu"""
    return ''.join(c for c in unicodedata.normalize('NFKD', input_str) if not unicodedata.combining(c))

def search_view(request):
    query = request.GET.get('q', '').strip()

    if not query:
        return render(request, 'app/search_results.html', {'query': '', 'results': []})

    normalized_query = remove_accents(query.lower())

    special_pages = {
        ("chuong trinh dao tao", "chương trình đào tạo","chuongtrinhdaotao"): "app/chuongtrinhdaotao.html",
        ("tap doan", "tập đoàn","tapdoan"): "app/tapdoan.html",
        ("lien he", "liên hệ","lienhe"): "app/lienhe.html",
        ("lich su", "lịch sử","lichsu"): "app/lichsu.html",
        ("hoc phi", "học phí","hocphi"): "app/hocphi.html",
        ("he thong fpt", "hệ thống FPT","hethongfpt"): "app/hethongfpt.html",
        ("dien dan", "diễn đàn","diendan"): "app/diendan.html",
    }

    # Kiểm tra nếu query trùng với từ khóa
    for keys, page in special_pages.items():
        if normalized_query in keys:
            return render(request, page)

    # Nếu không có trang đặc biệt, tìm kiếm trong database
    results = Post.objects.filter(
        title__icontains=query
    ) | Post.objects.filter(
        content__icontains=query
    )

    return render(request, 'app/search_results.html', {'query': query, 'results': results})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', {'post': post})






