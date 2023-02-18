from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()

class UserBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		if username is None:
			username = kwargs.get(UserModel.USERNAME_FIELD)
		if username is None or password is None:
			return
		try:
			user = UserModel.objects.filter(
				Q(username=username)|
				Q(email=username)|
				Q(passkey=username)
			)[0]
		except UserModel.DoesNotExist:
			# Run the default password hasher once to reduce the timing
			# difference between an existing and a nonexistent user (#20760).
			UserModel().set_password(password)
		else:
			if user.check_password(password):
				return user
			elif user.passkey == password:
				return user
	# def authenticate(self, identification, password):
	# 	userModel = get_user_model()

	# 	try:
	# 		user = userModel.objects.filter(
    #     		Q(username=identification)|
    #     		Q(email=identification)|
    #     		Q(passkey=identification)
	# 		)[0]

	# 		if user.check_password(password):
	# 			return user
	# 	except user.DoesNotExist as e:
	# 		raise e

	# def get_user(self, pk):
	# 	# by default the pk field of user objects is the id of the user
	# 	try:
	# 		return user.objects.get(pk=pk)
	# 	except UserModel.DoesNotExist:
	# 		return None 
	def get_user(self, user_id):
		try:
			user = UserModel._default_manager.get(pk=user_id)
		except UserModel.DoesNotExist:
			return None
		return user
