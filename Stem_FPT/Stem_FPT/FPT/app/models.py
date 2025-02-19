from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class AssignmentSubmission(models.Model):
    student_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.file.name}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Unknown")
    mssv = models.CharField(max_length=20, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    nam_hoc = models.CharField(max_length=10, blank=True, null=True)
    nam_sinh = models.CharField(max_length=4, blank=True, null=True)
    dia_chi_thuong_tru = models.TextField(blank=True, null=True)
    que_quan = models.TextField(blank=True, null=True)
    so_dien_thoai = models.CharField(max_length=15, blank=True, null=True)
    thong_tin_gia_dinh = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Kiểm tra nếu cần cập nhật thông tin User
        update_user = False
        user = self.user
        
        if user.first_name != self.name:
            user.first_name = self.name
            update_user = True

        if self.email and self.email != user.email:
            user.email = self.email
            update_user = True
        
        # Chỉ lưu User nếu có thay đổi
        if update_user:
            user.save(update_fields=['first_name', 'email'])

        super().save(*args, **kwargs)  # Lưu Profile




class SinhVien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Liên kết với user
    name = models.CharField(max_length=100)
    mssv = models.CharField(max_length=20)
    class_name = models.CharField(max_length=20)
    nam_hoc = models.CharField(max_length=10)
    nam_sinh = models.DateField()
    dia_chi_thuong_tru = models.CharField(max_length=255)
    que_quan = models.CharField(max_length=255)
    so_dien_thoai = models.CharField(max_length=20)
    email = models.EmailField()
    thong_tin_gia_dinh = models.TextField()

    def __str__(self):
        return self.name
    

class LienHe(models.Model):
    ho_ten = models.CharField(max_length=255)
    email = models.EmailField()
    loi_nhan = models.TextField()
    ngay_gui = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ho_ten} - {self.email}"
    


class DangKy(models.Model):
    ten_phu_huynh = models.CharField(max_length=255, default="Nhập tên phụ huynh")
    email = models.EmailField(default="Nhập email")
    so_dien_thoai = models.CharField(max_length=20, default="Nhập số điện thoại")
    truong = models.CharField(max_length=255, default="Nhập tên trường")
    nam_sinh = models.IntegerField(default=2000)  # Giả sử năm sinh mặc định là 2000
    tinh_thanh = models.CharField(max_length=50, default="Nhập tỉnh/thành phố")

    def __str__(self):
        return f'{self.ten_phu_huynh} - {self.email}'








