from django.db import models
from django.contrib.auth.models import AbstractUser
import string, random
from django.utils.translation import gettext as _

# Create your models here.

# django's default user has a username, first name, last name, email, password and password confirmation
class User(AbstractUser):
    # USER_TYPE_CHOICES = (
    #   (1, 'student'),
    #   (2, 'teacher'),
    #   (3, 'admin'),
    # )

    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
    username = models.CharField(_('Full Name'), max_length=100, blank=True, unique=True)

    is_teacher = models.BooleanField(default=False, null=True)
    is_student = models.BooleanField(default=False, null=True)
    passkey = models.CharField(
        max_length=10, 
        null=True, 
        default=''.join(random.sample(tuple(set((*string.ascii_letters, *string.digits))), 10)), 
        editable=False,
    )

class Subject(models.Model):
    name = models.CharField(max_length=100)
    pass_mark = models.IntegerField()

    def percentage(self):
        return self.score* self.pass_mark

    def __str__(self):
        return self.name

class Class(models.Model):
    label = models.CharField(max_length=15)

    def __str__(self):
        return self.label

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='student_profile')
    image = models.ImageField(upload_to = 'student_images')
    birth_date = models.DateField()
    _class = models.ForeignKey(Class, on_delete=models.PROTECT, related_name='students', null=True)
    subjects = models.ManyToManyField(Subject, related_name='offering_students')

    def __str__(self):
        return self.user.username


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='teacher_profile')
    image = models.ImageField(upload_to = 'teacher_images')
    phone = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username



class TermResult(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete = models.PROTECT, related_name='term_results')
    data = models.JSONField(null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student.user.username


class YearResult(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete = models.PROTECT, related_name='year_results')
    data = models.JSONField(null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student.user.username

