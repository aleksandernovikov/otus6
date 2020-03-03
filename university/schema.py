import graphene
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
    all_courses = graphene.List(CourseType, limit=graphene.Int())
    course = graphene.Field(CourseType, id=graphene.Int())

    all_teachers = graphene.List(TeacherType, limit=graphene.Int())
    all_students = graphene.List(StudentType, limit=graphene.Int())

    def resolve_all_courses(self, *args, **kwargs):
        return Course.objects.all()[:kwargs.get('limit')]

    def resolve_course(self, *args, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Course.objects.get(pk=id)
        return None

    def resolve_all_teachers(self, *args, **kwargs):
        return Teacher.objects.all()[:kwargs.get('limit')]

    def resolve_all_students(self, *args, **kwargs):
        return Student.objects.all()[:kwargs.get('limit')]
