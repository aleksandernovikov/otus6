import factory
from django.contrib.auth import get_user_model

from ..models import Student, Teacher, Course, Lesson


def ru_faker(*args, **kwargs):
    return factory.Faker(*args, **kwargs, locale='ru_RU')


User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = ru_faker('user_name')
    first_name = ru_faker('first_name')
    middle_name = ru_faker('middle_name')
    last_name = ru_faker('last_name')
    email = ru_faker('email')
    password = ru_faker('password')


class StudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def courses(self, create, courses, **kwargs):
        if courses:
            for course in courses:
                self.courses.add(course)


class TeacherFactory(factory.DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course

    title = ru_faker('text')

    @factory.post_generation
    def teachers(self, create, teachers, *args, **kwargs):
        if create:
            if not teachers:
                teachers_count = kwargs.get('teachers_count', 1)
                teachers = [TeacherFactory() for i in range(teachers_count)]
            for teacher in teachers:
                self.teachers.add(teacher)


class LessonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Lesson

    course = factory.SubFactory(CourseFactory)
    start_time = ru_faker('date_time')
