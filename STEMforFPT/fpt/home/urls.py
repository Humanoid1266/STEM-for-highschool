from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('tapdoan/', views.tapdoan, name='tapdoan'),
    path('lichsu/', views.lichsu, name='lichsu'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
