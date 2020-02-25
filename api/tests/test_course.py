from rest_framework import status
from rest_framework.test import APITestCase

from university.tests.factories import CourseFactory, TeacherFactory


class CourseTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.default = CourseFactory()

    def test_list_course(self):
        response = self.client.get('/api/v1/course/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        course = CourseFactory.build()
        response = self.client.post('/api/v1/course/', {
            'title': course.title
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = response.json()
        self.assertEqual(result.get('title'), course.title)

    def test_retrieve_course(self):
        response = self.client.get(f'/api/v1/course/{self.default.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json()
        self.assertEqual(result.get('title'), self.default.title)

    def test_update_course(self):
        teacher = TeacherFactory()
        response = self.client.patch(
            f'/api/v1/course/{self.default.pk}/', {'teachers': [teacher.pk]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_course(self):
        response = self.client.delete(f'/api/v1/course/{self.default.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
