import json

from graphene_django.utils import GraphQLTestCase

from otus6 import schema
from university.tests.factories import TeacherFactory


class TestTeacherGQL(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self) -> None:
        self.teacher = TeacherFactory()

    def test_query_all_teachers(self) -> None:
        response = self.query(
            '''
            {
              allTeachers {
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
