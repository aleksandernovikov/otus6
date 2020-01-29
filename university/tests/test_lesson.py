from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import make_aware

from .factories import CourseFactory, ru_faker, LessonFactory
from ..models import Lesson


class TestLesson(TestCase):
    def test_create(self):
        course = CourseFactory()
        start = ru_faker('date_time').generate()
        lesson = Lesson.objects.create(course=course, start_time=start)
        self.assertIsInstance(lesson, Lesson)
        self.assertEqual(lesson.course, course)
        self.assertEqual(lesson.start_time, start)

    def test_delete(self):
        lesson = LessonFactory()
        lesson_id = lesson.id
        self.assertIsInstance(lesson, Lesson)
        self.assertTrue(Lesson.objects.filter(pk=lesson_id).exists())
        Lesson.objects.filter(pk=lesson_id).delete()
        self.assertFalse(Lesson.objects.filter(pk=lesson_id).exists())

    def test_update_course(self):
        lesson = LessonFactory()
        old_course = lesson.course
        new_course = CourseFactory()
        lesson.course = new_course
        lesson.save(update_fields=('course',))
        lesson.refresh_from_db()
        self.assertNotEqual(old_course, lesson.course)

    def test_update_start_time(self):
        lesson = LessonFactory()
        old_value = lesson.start_time
        new_value = make_aware(old_value + timedelta(days=7))
        lesson.start_time = new_value
        lesson.save(update_fields=('start_time',))
        lesson.refresh_from_db()
        self.assertEqual(lesson.start_time, new_value)
