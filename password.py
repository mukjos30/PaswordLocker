import pyperclip

class User:
	'''
	Class to create user accounts and save their details
	'''


	def __init__(self,first_name,last_name,password):


		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	users_list = []
	def save_user(self):
		'''
		Method to save a newly created user into users_list.
		'''
		User.users_list.append(self)