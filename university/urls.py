from django.urls import path

from .views import CourseCreateView, CourseListView, CourseDeleteView, CourseUpdateView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('course/create/', CourseCreateView.as_view(), name='course-create'),
    path('course/delete/<int:pk>/', CourseDeleteView.as_view(), name='course-delete'),
    path('course/update/<int:pk>/', CourseUpdateView.as_view(), name='course-update'),
    path('course/detail/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
