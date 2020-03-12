from rest_framework import viewsets

from ..serializers.teacher import TeacherSerializer
from university.models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.prefetch_related('courses')
