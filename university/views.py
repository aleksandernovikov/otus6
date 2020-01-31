from django import views
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .forms import CourseForm
from .mixins import TitleViewMixin
from .models import Course


class CourseListView(TitleViewMixin, views.generic.ListView):
    model = Course
    template_name = 'university/course/course_list.html'
    page_title = _('Course list')


class CourseCreateView(TitleViewMixin, views.generic.CreateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('course-list')
    template_name = 'university/course/course_form.html'
    page_title = _('Course creation')


class CourseDeleteView(TitleViewMixin, views.generic.DeleteView):
    model = Course
    template_name = 'university/course/course_confirm_delete.html'
    success_url = reverse_lazy('course-list')
    page_title = _('Course deletion')


class CourseUpdateView(TitleViewMixin, views.generic.UpdateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('course-list')
    template_name = 'university/course/course_form.html'
    page_title = _('Course update')


class CourseDetailView(TitleViewMixin, views.generic.DetailView):
    model = Course
    template_name = 'university/course/course_detail.html'
    page_title = _('Course details')
