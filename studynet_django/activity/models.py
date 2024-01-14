from django.contrib.auth.models import User
from django.db import models

from course.models import Course, Lesson

class Activity(models.Model):
    STARTED = 'started'
    DONE = 'done'

    STATUS_CHOICES = (
        (STARTED, 'Started'),
        (DONE, 'Done')
    )

    couser = models.ForeignKey(Course, related_name='activities', on_delete=models.CASCADE)
    Losson = models.ForeignKey(Lesson, related_name='activities', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STARTED)
    created_by = models.ForeignKey(User, related_name='activities', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)