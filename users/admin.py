from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'email', 'is_superuser', 'passkey']

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    model = StudentProfile
    list_display = ['age', 'birth_date']

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    model = TeacherProfile
    list_display = ['phone', 'address']