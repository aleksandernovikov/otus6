import json

from graphene_django.utils import GraphQLTestCase

from otus6 import schema
from university.tests.factories import UserFactory


class UniversityUserTest(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self) -> None:
        self.user = UserFactory()

    def test_all_users(self) -> None:
        """
        Проверка получения всех пользователей
        """
        response = self.query(
            '''
            {
              allUsers {
                id
                firstName
                lastName
              }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_retrieve_user(self) -> None:
        """
        Проверка получения одного пользователя
        """
        response = self.query(
            '''
            query getUser($id: Int){
              user(id: $id){
                id
                firstName
                lastName
              }
            }
            ''', variables={'id': self.user.id}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        user = content.get('data').get('user')
        self.assertEqual(int(user.get('id')), self.user.id)
        self.assertEqual(user.get('firstName'), self.user.first_name)
        self.assertEqual(user.get('lastName'), self.user.last_name)

    def test_user_mutation(self) -> None:
        """
        Тест мутации пользователя
        """
        new_first_name, new_last_name = 'Test1', 'TestTest2'

        response = self.query(
            '''
            mutation update($id: ID, $firstName: String, $lastName: String){
              updateUser(id: $id,firstName: $firstName, lastName: $lastName ) {
                universityUser{
                  firstName
                  lastName
                }
              }
            }
            ''', variables={'id': self.user.id, 'firstName': new_first_name, 'lastName': new_last_name}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

        data = content.get('data')
        user_data = data.get('updateUser').get('universityUser')

        self.assertEqual(user_data.get('firstName'), new_first_name)
        self.assertEqual(user_data.get('lastName'), new_last_name)
