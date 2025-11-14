from django.db.models import Count, Q
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category
from courses.models import Course  # چون Course به Category FK دارد

# لیست دسته‌ها با شمارش دوره‌های منتشرشده
def category_list(request):
    q = request.GET.get('q', '')
    categories = (Category.objects
                  .annotate(course_count=Count('courses', filter=Q(courses__is_published=True)))
                  .order_by('name'))
    if q:
        categories = categories.filter(name__icontains=q)

    return render(request, 'categories/list.html', {
        'categories': categories,
        'q': q,
    })

# جزییات دسته + دوره‌ها با صفحه‌بندی
from django.shortcuts import render, get_object_or_404
from .models import Category
from courses.models import Course

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    
    # گرفتن دوره‌ها برای این دسته
    courses_qs = Course.objects.filter(category=category, is_published=True).order_by('-created_at')

    # صفحه‌بندی دوره‌ها
    paginator = Paginator(courses_qs, 8)  # هر صفحه 8 دوره
    page_number = request.GET.get('page')
    courses_page = paginator.get_page(page_number)

    # گرفتن زیرمجموعه‌ها (دسته‌های فرعی)
    subcats = category.children.all()

    return render(request, 'categories/detail.html', {
        'category': category,
        'subcats': subcats,
        'courses_page': courses_page,
    })
