from django.db import models
from django.contrib.auth.models import AbstractUser
import string, random

# Create your models here.

# django's default user has a username, first name, last name, email, password and password confirmation
class User(AbstractUser):
    # USER_TYPE_CHOICES = (
    #   (1, 'student'),
    #   (2, 'teacher'),
    #   (3, 'admin'),
    # )

    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
    username = models.CharField(max_length=100, blank=True)
    is_teacher = models.BooleanField(default=False, null=True)
    is_student = models.BooleanField(default=False, null=True)
    passkey = models.CharField(max_length=10, null=True, default=''.join(random.sample(tuple(set((*string.ascii_letters, *string.digits))), 10)))

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='student_profile')
    image = models.ImageField(upload_to = 'student_images')
    age = models.IntegerField()
    birth_date = models.DateField()


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='teacher_profile')
    image = models.ImageField(upload_to = 'teacher_images')
    phone = models.IntegerField()
    address = models.CharField(max_length=200)

