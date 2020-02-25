from rest_framework import viewsets

from ..serializers.course import CourseSerializer
from university.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
