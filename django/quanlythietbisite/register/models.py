from django.db import models

# Create your models here.
class NGUOIDUNG(models.Model):
    tendangnhap = models.CharField(max_length=50, unique=True)
    matkhau = models.CharField(max_length=50)