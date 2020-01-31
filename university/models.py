from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from university.mixins import UserRepresentationModelMixin


class Course(models.Model):
    """
    Учебный курс
    """
    title = models.CharField(_('Course title'), max_length=128)

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
        return self.students.all()


class Teacher(UserRepresentationModelMixin, models.Model):
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


class Student(UserRepresentationModelMixin, models.Model):
    """
    Студент
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))

    courses = models.ManyToManyField(
        Course,
        related_name='students',
        verbose_name=_('Courses'),
        blank=True
    )

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def enroll_in_a_course(self, course):
        """
        Записаться на курс
        """
        self.courses.add(course)


class Lesson(models.Model):
    """
    Занятие на курсе
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    start_time = models.DateTimeField(_('Lesson start time'))

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return f'{self.course} {self.start_time}'
