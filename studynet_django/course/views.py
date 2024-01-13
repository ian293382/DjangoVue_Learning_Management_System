from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Course, Lesson, Comment,Category
from .serializers import CourseListSerializer, CourseDetailSerializer, LessonsListSerializer, CommentSerializer,CategorySerializer

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_courses(request):
    # 如果有 category_id 則用 courses filter  如果沒有courses.get.all()
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.all()

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])

    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_frontpage_courses(request):
    courses = Course.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonsListSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    }

    return Response(data)

@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.get('name')
    content = data.get('content')

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(course=course, lesson=lesson, name=name, content=content, created_by=request.user)

    serializer = CommentSerializer(comment)

    return Response(serializer.data)


