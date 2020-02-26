from rest_framework import status
from rest_framework.test import APITestCase, APITransactionTestCase

from university.models import Course
from university.tests.factories import CourseFactory, TeacherFactory


class CourseTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.default = CourseFactory()

    def setUp(self) -> None:
        self.base_url = '/api/v1/course/'

    def test_list_course(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        course = CourseFactory.build()
        response = self.client.post(self.base_url, {
            'title': course.title
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = response.json()
        self.assertEqual(result.get('title'), course.title)

    def test_retrieve_course(self):
        response = self.client.get(f'{self.base_url}{self.default.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json()
        self.assertEqual(result.get('title'), self.default.title)

    def test_update_course(self):
        teacher = TeacherFactory()
        response = self.client.patch(
            f'{self.base_url}{self.default.pk}/', {'teachers': [teacher.pk]}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_course(self):
        response = self.client.delete(f'{self.base_url}{self.default.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TransactionCourseTest(APITransactionTestCase):

    def test_course_complete(self):
        CourseFactory()
        course = Course.objects.first()
        course.complete()
        self.assertTrue(course.finished)
