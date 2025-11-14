# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import rotate_token
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile


def register(request):
    """ثبت‌نام کاربر جدید"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            messages.success(request, "ثبت‌نام با موفقیت انجام شد.")
            return redirect('users:profile')  # :white_check_mark: این مسیر باید وجود داشته باشه
        else:
            messages.error(request, "ورودی‌ها نامعتبر است.")
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})



def user_login(request):
    """ورود کاربر با AuthenticationForm"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) # <-- اینجا حتما user رو پاس میدیم
            rotate_token(request)
            messages.success(request, f"خوش آمدید {user.username}!")
            return redirect('users:profile')
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
            return redirect('users:login')
    else:
        form = AuthenticationForm(request)

    return render(request, 'users/login.html', {'form': form})


@login_required
def profile(request):
    """نمایش و ویرایش پروفایل"""
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "پروفایل شما به‌روز شد.")
            return redirect('users:profile')
        else:
            messages.error(request, "خطا در ذخیره پروفایل.")
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'users/profile.html', {'form': form})


def user_logout(request):
    """خروج کاربر"""
    auth_logout(request)
    messages.info(request, "با موفقیت خارج شدید.")
    return redirect('blog:home')  # یا هر صفحه‌ای که می‌خوای بعد از خروج بره