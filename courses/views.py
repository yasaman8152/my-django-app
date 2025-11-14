from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Course



def course_list(request):
    courses = Course.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'courses/list.html', {'courses': courses})

# 📘 نمایش جزئیات یک دوره
def course_detail(request, slug):
    # دریافت دوره با استفاده از slug
    course = get_object_or_404(Course, slug=slug, is_published=True)

    # پیش‌پردازش سرفصل‌ها و تقسیم آن‌ها به لیست
    syllabus_list = course.syllabus.split("\n")  # تبدیل سرفصل‌ها به لیست

    # ارسال اطلاعات دوره و توضیحات موسسه به قالب
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'about_institute': settings.ABOUT_INSTITUTE_TEXT,  # ارسال توضیحات موسسه از تنظیمات
        'syllabus_list': syllabus_list  # ارسال لیست سرفصل‌ها به قالب
    })


def add_to_cart(request, id):
    # دریافت دوره بر اساس ID
    course = Course.objects.get(id=id)

    # فرض کنید که سبد خرید در session ذخیره می‌شود (این یک پیاده‌سازی ساده است)
    cart = request.session.get('cart', [])
    cart.append(course.id)
    request.session['cart'] = cart

    return redirect('course_detail', slug=course.slug)