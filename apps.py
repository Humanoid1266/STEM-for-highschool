from django.apps import AppConfig

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'  # Đổi 'app' thành tên ứng dụng của bạn

    def ready(self):
        import app.signals  # Đảm bảo Django tải signals
