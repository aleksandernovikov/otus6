from rest_framework import serializers

from university.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = 'id', 'title', 'teachers', 'start_date', 'end_date'
