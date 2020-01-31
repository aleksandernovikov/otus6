from django import forms

from university.models import Course, Lesson


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = (
            'course',
            'start_time',
        )
