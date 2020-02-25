from rest_framework import serializers

from .user import UserSerializer
from university.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = 'id', 'user', 'courses'
