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
    autocomplete_fields = ('teachers',)
    search_fields = ('title',)
    list_filter = ('teachers', 'start_date', 'end_date')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (TeacherCoursesInlineAdmin,)
    list_filter = ('courses',)
    autocomplete_fields = ('user',)

    search_fields = (
        'user__username',
        'user__first_name',
        'user__middle_name',
        'user__last_name'
    )

    ordering = ('id',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ('courses', 'user')
    list_filter = ('courses',)
    search_fields = (
        'user__username',
        'user__first_name',
        'user__middle_name',
        'user__last_name'
    )

    ordering = ('id',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = ('start_time', 'current_teacher')
    fields = (
        'course',
        'start_time',
        'end_time',
        'current_teacher'
    )
    autocomplete_fields = ('course', 'current_teacher')
