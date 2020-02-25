from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from university.mixins import UserRepresentationModelMixin

User = get_user_model()


class Course(models.Model):
    """
    Учебный курс
    """
    title = models.CharField(_('Course title'), max_length=128)

    teachers = models.ManyToManyField(
        'Teacher',
        verbose_name=_('Teachers'),
        related_name='courses',
    )

    start_date = models.DateField(_('Сourse start date'), default=datetime.now, blank=True, null=True)
    end_date = models.DateField(_('Course end date'), blank=True, null=True)

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.title


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
    end_time = models.DateTimeField(_('Lesson end time'), blank=True)

    current_teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name=_('Current teacher'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        format = "%d.%m.%y %H:%M"
        return f'{self.course} {self.start_time.strftime(format)} - {self.end_time.strftime(format)}'
