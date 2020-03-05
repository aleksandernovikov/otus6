from typing import List, Union, Optional

import graphene
from django.db.models import QuerySet
from graphene_django import DjangoObjectType

from .models import Course, Teacher, Student


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query:
    all_courses: graphene.List = graphene.List(CourseType, limit=graphene.Int())
    course: graphene.Field = graphene.Field(CourseType, id=graphene.Int())

    all_teachers: graphene.List = graphene.List(TeacherType, limit=graphene.Int())
    all_students: graphene.List = graphene.List(StudentType, limit=graphene.Int())

    @staticmethod
    def resolve_all_courses(*args: str, **kwargs: int) -> Union[QuerySet, List[Course]]:
        """
        Получение всех курсов
        """
        return Course.objects.all()[:kwargs.get('limit')]

    @staticmethod
    def resolve_course(*args: str, **kwargs: int) -> Optional[Course]:
        """
        Получение одного курса
        """
        pk: int = kwargs.get('id')
        if pk is not None:
            return Course.objects.get(pk=pk)
        return None

    @staticmethod
    def resolve_all_teachers(*args: str, **kwargs: int) -> Union[QuerySet, List[Teacher]]:
        """
        Получение всех учителей
        """
        return Teacher.objects.all()[:kwargs.get('limit')]

    @staticmethod
    def resolve_all_students(*args: str, **kwargs: int) -> Union[QuerySet, List[Student]]:
        """
        Получение всех студентов
        """
        return Student.objects.all()[:kwargs.get('limit')]
