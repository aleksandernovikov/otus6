from rest_framework.routers import DefaultRouter

from .views.course import CourseViewSet
from .views.lesson import LessonViewSet
from .views.student import StudentViewSet
from .views.teacher import TeacherViewSet
from .views.user import UserViewSet

api_router = DefaultRouter()
api_router.register('course', CourseViewSet, basename='course')
api_router.register('lesson', LessonViewSet, basename='lesson')
api_router.register('student', StudentViewSet, basename='student')
api_router.register('teacher', TeacherViewSet, basename='teacher')
api_router.register('user', UserViewSet, basename='user')

urlpatterns = api_router.urls
