from django.urls import path

from .views import CourseCreateView, CourseListView, CourseDeleteView, CourseUpdateView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='courses'),
    path('course/create/', CourseCreateView.as_view(), name='create-course'),
    path('course/delete/<int:pk>/', CourseDeleteView.as_view(), name='delete-course'),
    path('course/update/<int:pk>/', CourseUpdateView.as_view(), name='update-course'),
    path('course/detail/<int:pk>/', CourseDetailView.as_view(), name='course-details'),
]
