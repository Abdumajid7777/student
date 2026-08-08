from django.contrib import admin
from .models import Student, StudentMark, Group, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id", "first_name", "last_name", "age", "phone_numbers", 
        "group",
    )
    list_display_links = ("id", "first_name")
    search_fields = ("first_name", "last_name", "age", "phone_numbers")
    list_filter = ("group",)
    list_per_page = 3



@admin.register(StudentMark)
class StudentMarkAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "mark")
    search_fields = ("id", "student")
    list_display_links = ("id", "student")
    list_filter = ("mark", )



@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "start_date", "student_count", "mentor", )
    search_fields = ("name", "course", "mentor__first_name")
    list_filter = ("mentor", )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "director",)
    search_fields = ("name", "director")
    list_filter = ("director", )



