from django.contrib import admin
from .models import Course

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at')
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}