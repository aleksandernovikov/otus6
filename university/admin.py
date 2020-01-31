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


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (TeacherCoursesInlineAdmin,)
    # https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = (
        'user__username',
        'user__first_name',
        'user__middle_name',
        'user__last_name'
    )

    # ordering = ('id',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(age=search_term_as_int)
        return queryset, use_distinct


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
