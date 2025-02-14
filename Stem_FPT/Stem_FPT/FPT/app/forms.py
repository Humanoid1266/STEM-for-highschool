from django import forms
from .models import SinhVien
from .models import Profile
from .models import DangKy

class SinhVienForm(forms.ModelForm):
    class Meta:
        model = SinhVien
        fields = ['name', 'mssv', 'class_name', 'nam_hoc', 'nam_sinh', 'dia_chi_thuong_tru', 'que_quan', 'so_dien_thoai', 'email', 'thong_tin_gia_dinh']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'mssv', 'class_name', 'nam_hoc', 'nam_sinh', 'dia_chi_thuong_tru', 'que_quan', 'so_dien_thoai', 'email', 'thong_tin_gia_dinh']

class FormDangKy(forms.ModelForm):
    class Meta:
        model = DangKy
        fields = ['ten_phu_huynh', 'email', 'so_dien_thoai', 'truong', 'nam_sinh', 'tinh_thanh']