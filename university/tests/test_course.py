from django.test import TestCase

from ..models import Course
from .factories import ru_faker, TeacherFactory, CourseFactory


class TestCourse(TestCase):

    def test_create(self):
        title = ru_faker('word').generate()
        course = Course.objects.create(title=title)

        self.assertIsInstance(course, Course)
        self.assertEqual(course.title, title)

    def test_delete(self):
        course = CourseFactory()
        self.assertIsInstance(course, Course)

        course_id = course.id
        self.assertTrue(Course.objects.filter(id=course_id).exists())

        Course.objects.filter(id=course_id).delete()
        self.assertFalse(Course.objects.filter(id=course_id).exists())

    def test_update_course_title(self):
        course = CourseFactory()
        new_title = " ".join(ru_faker('words').generate())
        course.title = new_title
        course.save(update_fields=('title',))
        course.refresh_from_db()
        self.assertEqual(new_title, course.title)

    def test_add_course_teacher(self):
        course = CourseFactory()
        new_teacher = TeacherFactory()

        course.teachers.add(new_teacher)
        course.refresh_from_db()
        self.assertIn(new_teacher, course.teachers.all())

    def test_remove_teacher_from_course_(self):
        course = CourseFactory()
        new_teacher = TeacherFactory()

        course.teachers.add(new_teacher)
        course.refresh_from_db()
        self.assertIn(new_teacher, course.teachers.all())

        course.teachers.remove(new_teacher)
        course.refresh_from_db()
        self.assertNotIn(new_teacher, course.teachers.all())
