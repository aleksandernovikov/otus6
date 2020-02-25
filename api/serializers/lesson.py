from rest_framework import serializers

from university.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = 'id', 'course', 'start_time', 'end_time', 'current_teacher'
