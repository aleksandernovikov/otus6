from django.contrib import admin

from university.models import Course, Teacher, Student, Lesson


class StudentInlineAdmin(admin.TabularInline):
    model = Student.courses.through
    extra = 1


class TeacherCoursesInlineAdmin(admin.TabularInline):
    model = Course
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = (StudentInlineAdmin,)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (TeacherCoursesInlineAdmin,)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('courses',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass
