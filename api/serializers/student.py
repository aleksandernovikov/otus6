from rest_framework import serializers

from api.serializers.user import UserSerializer
from university.models import Student


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = 'id', 'user', 'courses'
