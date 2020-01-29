from django.test import TestCase

from ..models import Course
from .factories import ru_faker, TeacherFactory, CourseFactory, StudentFactory


class TestCourse(TestCase):

    def test_create(self):
        teacher = TeacherFactory()
        title = ru_faker('word').generate()
        course = Course.objects.create(title=title, teacher=teacher)

        self.assertIsInstance(course, Course)
        self.assertEqual(course.teacher, teacher)
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

    def test_update_course_teacher(self):
        course = CourseFactory()
        new_teacher = TeacherFactory()
        course.teacher = new_teacher
        course.save(update_fields=('teacher',))
        course.refresh_from_db()
        self.assertEqual(new_teacher, course.teacher)

    def test_students_list(self):
        course = CourseFactory()
        student = StudentFactory()
        self.assertNotIn(student, course.students_list())
        course.students.add(student)
        self.assertIn(student, course.students_list())
