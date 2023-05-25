from django.shortcuts import render
from django.http import HttpResponse
from .forms import register_form
from .models import NGUOIDUNG

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            tendangnhap = form.cleaned_data['tendangnhap']
            matkhau = form.cleaned_data['matkhau']
            if NGUOIDUNG.objects.filter(tendangnhap=tendangnhap).exists():
                form.add_error('tendangnhap', 'Tên đăng nhập đã tồn tại')
            else:
                user = NGUOIDUNG(tendangnhap=tendangnhap, matkhau=matkhau)
                user.save()
                return HttpResponse("Dang ki thanh cong")
    else:
        form = register_form()
    return render(request, "register/index.html", {'form': form})