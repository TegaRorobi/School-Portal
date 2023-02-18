from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from django.views.generic import *
from .forms import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os, smtplib, ssl

class UserCreateView(View):
	def get(self, request):
		form = StudentCreateForm() if request.GET.get('account_type')=='student' else TeacherCreateForm()
		return render(request, 'users/create.html', {'form':form})
	def post(self, request):
		# print(dir(request))
		print(request.POST)
		# print(request.FILES)
		if request.GET.get('account_type')=='student': 
			form = StudentCreateForm(request.POST, request.FILES) 
		else:
			form = TeacherCreateForm(request.POST, request.FILES)

		if form.is_valid():
			# print(dir(form))
			print('the form passed the valid check')
			user = form.save(commit=False)

			if request.GET.get('account_type')=='student': 
				new_user = User(
					username=request.POST.get('name'), 
					email=request.POST.get('email'), 
					is_student=True
				)
				new_user.is_superuser=True
				new_user.is_staff=True
				# print(new_user)
				new_user.set_password(request.POST.get('password'))
				new_user.save()
			else:
				new_user = User(
					username=request.POST.get('name'), 
					email=request.POST.get('email'), 
					is_teacher=True
				)
				new_user.is_superuser=True
				new_user.is_staff=True
				# print(new_user)
				new_user.set_password(request.POST.get('password'))
				new_user.save()

			user.user = new_user
			user.save()

			msg = MIMEMultipart()
			msg['Subject'] = 'Thanks for registering'
			msg['From']  = 'School Website'
			msg.attach(MIMEText(f"""
Hello {new_user.username}, thanks for registering a user account, 

You can log in to the account with your username or email as the identifier, 
and the password you set or a passkey created just for you.

Your passkey is {new_user.passkey}.

Thanks,
School Name

""", 'html'))
			with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp_server:
				smtp_server.login('deciphrexx2022@gmail.com', os.environ.get('EMAIL_PASSWORD'))
				smtp_server.sendmail('deciphrexx2022@gmail.com', 'deciphrexx@gmail.com', msg.as_string())
			print('success!')


		return redirect('/')
