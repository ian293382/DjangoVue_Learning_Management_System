from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from course import views
 # 特例寫在上方 因為slug也會包含到get_frontpage_courses
urlpatterns = [
    path('', views.get_courses),
    path('get_frontpage_courses/', views.get_frontpage_courses),
    path('get_categories/', views.get_categories), 
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<slug:lesson_slug>/get-comments/', views.get_comments),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)