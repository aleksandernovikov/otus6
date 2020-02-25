from rest_framework import viewsets

from ..serializers.lesson import LessonSerializer
from university.models import Lesson


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
