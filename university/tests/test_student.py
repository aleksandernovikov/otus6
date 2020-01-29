from django.test import TestCase

from .factories import UserFactory, StudentFactory, CourseFactory
from ..models import Student


class TestStudent(TestCase):
    def test_create(self):
        user = UserFactory()
        student = Student.objects.create(user=user)
        self.assertIsInstance(student, Student)
        self.assertEqual(student.user, user)

    def test_delete(self):
        student = StudentFactory()
        student_id = student.id
        self.assertTrue(Student.objects.filter(pk=student_id).exists())
        Student.objects.filter(pk=student_id).delete()
        self.assertFalse(Student.objects.filter(pk=student_id).exists())

    def test_user_replace(self):
        student = StudentFactory()
        new_user = UserFactory()
        student.user = new_user
        student.save(update_fields=('user',))
        student.refresh_from_db()
        self.assertEqual(student.user, new_user)

    def test_change_username(self):
        student = StudentFactory()
        new_username = 'new_username'
        student.user.username = new_username
        student.save(update_fields=('user',))
        self.assertEqual(student.user.username, new_username)

    def test_enroll_in_a_course(self):
        student = StudentFactory()
        course = CourseFactory()
        self.assertNotIn(course, student.courses.all())
        student.enroll_in_a_course(course)
        self.assertIn(course, student.courses.all())
