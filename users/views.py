from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
import json

# imports directly related to email sending
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os, smtplib, ssl

class UserCreateView(View):
	def get(self, request):
		form = StudentCreateForm() if request.GET.get('account_type')=='student' else TeacherCreateForm()
		return render(request, 'users/register.html', {'form':form})
	def post(self, request):
		print(request.POST)
		account_type =  request.GET.get('account_type')
		form = StudentCreateForm(request.POST, request.FILES) if account_type =='student' else TeacherCreateForm(request.POST, request.FILES)
		if form.is_valid():
			user_profile = form.save(commit=False)
			user = User(username=request.POST.get('name'), email=request.POST.get('email'))
			if account_type =='student': 
				user.is_student = True
			elif account_type =='teacher':
				user.is_teacher = True
			user.set_password(request.POST.get('password'))
			user.save()
			user_profile.user = user
			user_profile.save()

			login(request, user)

			msg = MIMEMultipart()
			msg['Subject'] = 'Thanks for registering'
			msg['From']  = 'School Name'
			msg.attach(MIMEText(f"""
<h4>Hello {user.username}, your account has been registered successfully!</h4>

<p>Your user account has been authenticated and you can now login at (site_login_url) using either your username or email as the identifier and your password.</p>

<p>Just in case you forget the password, here is a unique passkey you can use to login to your account:</p>
<strong>{user.passkey}</strong>

<p>Thanks for choosing us, </p>
<p>(school_name)</p>
""", 'html'))

			with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp_server:
				smtp_server.login('deciphrexx2022@gmail.com', os.environ.get('EMAIL_PASSWORD'))
				smtp_server.sendmail('deciphrexx2022@gmail.com', 'deciphrexx@gmail.com', msg.as_string())
			print('User registration complete')
		else:print('The form is not valid')

		return redirect('/')

class UserLoginView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'users/login.html', {})
	def post(self, request, *args, **kwargs):
		print(request.POST)
		if request.POST.get('login_btn'):
			username, password = request.POST.get('username'), request.POST.get('password')
			try:
				user_object = authenticate(request, username=username, password=password)
				if user_object:
					login(request, user_object)
					messages.success(request, f'{user_object.username} has been logged in successfully')
			except User.DoesNotExist:
				messages.error(request, 'Invalid username or password')
		return self.get(request)

class UserLogoutView(View):
	def get(self, request):
		logout(request, request.user)
		return redirect(reverse('login'))

def jsonresponse(request):
	subject_list = Subject.objects.values()
	print(Subject.objects.all())
	print(Subject.objects.values())
	return JsonResponse(list(subject_list), safe=False)

