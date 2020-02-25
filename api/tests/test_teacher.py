from rest_framework import status
from rest_framework.test import APITestCase

from university.tests.factories import UserFactory, TeacherFactory


class TestTeacher(APITestCase):
    def setUp(self) -> None:
        self.teacher = TeacherFactory()
        self.user = UserFactory()

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.base_url = '/api/v1/teacher/'

    def test_list_teacher(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_teacher(self):
        response = self.client.post(self.base_url, {'user': self.user.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_teacher(self):
        response = self.client.get(f'{self.base_url}{self.teacher.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_teacher(self):
        new_user = UserFactory()
        response = self.client.patch(
            f'{self.base_url}{self.teacher.pk}/',
            {'user': new_user.pk}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_teacher(self):
        response = self.client.delete(f'{self.base_url}{self.teacher.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
