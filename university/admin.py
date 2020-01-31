from django.contrib import admin

from .models import Course, Teacher, Student, Lesson


class StudentInlineAdmin(admin.TabularInline):
    model = Student.courses.through
    extra = 1


class TeacherCoursesInlineAdmin(admin.TabularInline):
    model = Course.teachers.through
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = (StudentInlineAdmin,)
    filter_horizontal = ('teachers',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (TeacherCoursesInlineAdmin,)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ('courses',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fields = (
        'course',
        'start_time',
        'end_time',
        'current_teacher'
    )
    readonly_fields = ('end_time',)

    # def get_end_time(self, obj):
    #     return obj.end_time
