from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from university.mixins import UserReprMixin


class Course(models.Model):
    """
    Учебный курс
    """
    title = models.CharField(_('Course name'), max_length=128)

    teacher = models.ForeignKey(
        'Teacher',
        on_delete=models.CASCADE,
        verbose_name=_('Teacher'),
        related_name='courses',
    )

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.title

    def students_list(self):
        return self.student_set.all()


class Teacher(UserReprMixin, models.Model):
    """
    Преподаватель
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def teaches_courses(self):
        return self.courses.all()


class Student(UserReprMixin, models.Model):
    """
    Студент
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))

    courses = models.ManyToManyField(
        Course,
        verbose_name=_('Courses'),
        blank=True
    )

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def enroll_in_a_course(self, course):
        self.courses.add(course)


class Lesson(models.Model):
    """
    Занятие на курсе
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField(_('Lesson start time'))

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
