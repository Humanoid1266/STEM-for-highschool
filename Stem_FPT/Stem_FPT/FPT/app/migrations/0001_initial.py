# Generated by Django 5.0.11 on 2025-02-04 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mssv', models.CharField(blank=True, max_length=20, null=True)),
                ('class_name', models.CharField(blank=True, max_length=50, null=True)),
                ('nam_hoc', models.CharField(blank=True, max_length=10, null=True)),
                ('nam_sinh', models.CharField(blank=True, max_length=4, null=True)),
                ('dia_chi_thuong_tru', models.TextField(blank=True, null=True)),
                ('que_quan', models.TextField(blank=True, null=True)),
                ('so_dien_thoai', models.CharField(blank=True, max_length=15, null=True)),
                ('thong_tin_gia_dinh', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
