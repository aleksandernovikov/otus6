import json

from graphene_django.utils import GraphQLTestCase

from otus6 import schema
from university.tests.factories import CourseFactory


class TestCourseGQL(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self) -> None:
        self.course = CourseFactory()

    def test_query_all_courses(self) -> None:
        response = self.query(
            '''
            {
              allCourses {
                id
                title    
              }
            }
            ''')
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_retrieve_one_course(self) -> None:
        response = self.query(
            '''
            query ($id: Int) {
                course(id: $id) {
                    id
                    title
                }
            }
            ''', variables={'id': self.course.id}
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
