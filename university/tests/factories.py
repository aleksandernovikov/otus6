import factory
from django.contrib.auth.models import User

from ..models import Student, Teacher, Course, Lesson


def ru_faker(*args, **kwargs):
    return factory.Faker(*args, **kwargs, locale='ru_RU')


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = ru_faker('user_name')
    first_name = ru_faker('first_name')
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
    teacher = factory.SubFactory(TeacherFactory)


class LessonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Lesson

    course = factory.SubFactory(CourseFactory)
    start_time = ru_faker('date_time')
