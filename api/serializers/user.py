from rest_framework import serializers

from custom_user.models import UniversityUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityUser
        fields = 'id', 'first_name', 'middle_name', 'last_name', 'display_name'
