from rest_framework import viewsets

from ..serializers.user import UserSerializer
from custom_user.models import UniversityUser


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UniversityUser.objects.all()
