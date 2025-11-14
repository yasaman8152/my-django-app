from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses'
    )
    description = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    video_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hours = models.IntegerField()
    syllabus = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('courses:course_detail', kwargs={'slug': self.slug})

