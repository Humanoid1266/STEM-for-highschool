from django.contrib import admin
from .models import LienHe
from .models import DangKy
from .models import AssignmentSubmission

@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'file', 'submitted_at')

@admin.register(LienHe)
class LienHeAdmin(admin.ModelAdmin):
    list_display = ('ho_ten', 'email', 'loi_nhan', 'ngay_gui')  # Hiển thị thêm lời nhắn
    search_fields = ('ho_ten', 'email', 'loi_nhan')  # Cho phép tìm kiếm theo lời nhắn
    list_filter = ('ngay_gui',)  # Bộ lọc theo ngày gửi

class DangKyAdmin(admin.ModelAdmin):
    list_display = ('ten_phu_huynh', 'email', 'so_dien_thoai', 'truong', 'nam_sinh', 'tinh_thanh')  # Các trường sẽ hiển thị trên trang danh sách
    search_fields = ('ten_phu_huynh', 'email', 'so_dien_thoai')  # Cho phép tìm kiếm theo tên, email, số điện thoại
    list_filter = ('tinh_thanh',)  # Lọc theo Tỉnh/Thành phố

# Đăng ký mô hình và lớp quản trị vào admin
admin.site.register(DangKy, DangKyAdmin)

