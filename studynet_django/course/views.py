from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Course
from .serializers import CourseListSerializer


@api_view(['GET'])
def get_coursse(request):
    courses = Course.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)