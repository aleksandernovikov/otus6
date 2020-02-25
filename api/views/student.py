from rest_framework import viewsets

from university.models import Student
from ..serializers.student import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
