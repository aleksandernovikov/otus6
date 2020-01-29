from django.test import TestCase

from ..models import Teacher
from .factories import UserFactory, TeacherFactory, CourseFactory


class TestTeacher(TestCase):
    def test_create(self):
        user = UserFactory()
        teacher = Teacher.objects.create(user=user)
        self.assertIsInstance(teacher, Teacher)
        self.assertEqual(teacher.user, user)

    def test_delete(self):
        teacher = TeacherFactory()
        teacher_id = teacher.id
        self.assertTrue(Teacher.objects.filter(pk=teacher_id).exists())
        Teacher.objects.filter(pk=teacher_id).delete()
        self.assertFalse(Teacher.objects.filter(pk=teacher_id).exists())

    def test_update(self):
        new_user = UserFactory()
        teacher = TeacherFactory()
        self.assertNotEqual(new_user, teacher.user)
        teacher.user = new_user
        teacher.save(update_fields=('user',))
        teacher.refresh_from_db()
        self.assertEqual(new_user, teacher.user)

    def test_teaches_courses(self):
        teacher = TeacherFactory()
        new_course = CourseFactory()
        self.assertNotIn(new_course, teacher.teaches_courses())
        teacher.courses.add(new_course)
        self.assertIn(new_course, teacher.teaches_courses())
