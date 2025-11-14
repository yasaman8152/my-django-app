from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'category', 'description', 'content', 'video_url', 'price', 'hours', 'syllabus', 'about_institute']
