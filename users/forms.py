from django import forms
from .models import *

# Create your forms here.

class StudentCreateForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = '__all__'
		exclude = ['user', 'passkey']

class TeacherCreateForm(forms.ModelForm):
	first_name = forms.TextInput()
	last_name = forms.TextInput()
	class Meta:
		model = TeacherProfile
		fields = '__all__'
		exclude = ['user', 'passkey']

