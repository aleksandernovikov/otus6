from rest_framework.routers import DefaultRouter

from .views.course import CourseViewSet
from .views.teacher import TeacherViewSet
from .views.user import UserViewSet

api_router = DefaultRouter()
api_router.register('course', CourseViewSet, basename='course')
api_router.register('teacher', TeacherViewSet, basename='teacher')
api_router.register('user', UserViewSet, basename='user')

urlpatterns = api_router.urls
