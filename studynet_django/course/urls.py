from django.urls import path

from course import views

urlpatterns = [
    path('', views.get_courses),
    # 特例寫在上方 因為slug也會包含到get_frontpage_courses
    path('get_frontpage_courses/', views.get_frontpage_courses), 
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments/', views.get_comments),
]