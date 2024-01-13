from django.contrib import admin

from .models import Category, Course, Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'status', 'lesson_type']
    list_filter = ['status', 'lesson_type']

admin.site.register(Category)

admin.site.register(Course)

admin.site.register(Lesson, LessonAdmin)