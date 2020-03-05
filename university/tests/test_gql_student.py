import json

from graphene_django.utils import GraphQLTestCase

from otus6 import schema
from university.tests.factories import StudentFactory


class TestStudentGQL(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self) -> None:
        self.student = StudentFactory()

    def test_query_all_students(self) -> None:
        """
        Тест получения всех студентов
        """
        response = self.query(
            '''
            {
              allStudents {
                id
                user {
                  id
                  firstName
                  lastName
                }    
              }
            }
            ''')
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
