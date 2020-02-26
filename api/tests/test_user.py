from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase, APIRequestFactory

from api.views.user import UserViewSet
from university.tests.factories import UserFactory, ru_faker

User = get_user_model()


class TestUserSimple(APISimpleTestCase):
    def test_create_user_factory(self):
        username = 'test_user'
        user = UserFactory.build(username=username)
        self.assertEqual(user.username, username)


class TestUser(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()

    @classmethod
    def setUpTestData(cls):
        cls.base_url = '/api/v1/user/'

    def test_list_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.get(self.base_url)
        user_view = UserViewSet.as_view({'get': 'list'})
        response = user_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_request_factory(self):
        u = UserFactory.build()
        request_factory = APIRequestFactory()
        request = request_factory.post(
            self.base_url,
            {
                'username': u.username,
                'first_name': u.first_name,
                'middle_name': u.middle_name,
                'last_name': u.last_name
            }
        )
        user_view = UserViewSet.as_view({'post': 'create'})
        response = user_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.get(f'{self.base_url}{self.user.pk}/')
        user_view = UserViewSet.as_view({'get': 'retrieve'})
        response = user_view(request, pk=self.user.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_request_factory(self):
        request_factory = APIRequestFactory()
        new_first_name = ru_faker('first_name').generate()
        request = request_factory.patch(
            f'{self.base_url}{self.user.pk}/',
            {
                'first_name': new_first_name
            })
        user_view = UserViewSet.as_view({'patch': 'partial_update'})
        response = user_view(request, pk=self.user.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.delete(f'{self.base_url}{self.user.pk}/')
        user_view = UserViewSet.as_view({'delete': 'destroy'})
        response = user_view(request, pk=self.user.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
