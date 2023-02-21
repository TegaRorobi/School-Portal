from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'email', 'is_teacher', 'is_student', 'passkey']

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    model = StudentProfile
    list_display = ['name', 'birth_date']
    @admin.display()
    def name(self, obj):
        return obj.user.username

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    model = TeacherProfile
    list_display = ['name', 'phone', 'address']
    @admin.display()
    def name(self, obj):
        return obj.user.username

admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(TermResult)
admin.site.register(YearResult)