import pyperclip #importing pyperclip for copying to clipboard
from password import User #importing user class 
import random #import random variable generator
import string  #import string constants

class Credential:
	'''
	Class to create  account credentials, generate new passwords and save user information
	'''

	list_of_credentials =[]
	user_credentials_list = []

	def __init__(self,username,credential_account,account_name,password):
		'''
		Method to define the properties for each user object.
		'''

		self.username = username
		self.credential_account = credential_account = credential_account
		self.account_name = account_name
		self.password = password

	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered exist in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	
	def save_credentials(self):
		'''
		Function to save a newly created user credentials
		'''

		Credential.list_of_credentials.append(self)
  
	@classmethod
	def delete_credentials(self):
		'''
		Function to delete  credentials
		'''

		Credential.list_of_credentials.remove(self)
  

	def generate_password(size=8, char=string.ascii_lowercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate a secure 8 character password for a user.
		'''
		password_gen=''.join(random.choice(char) for _ in range(size))
		return password_gen

	@classmethod
	def display_credentials(cls,username):
		'''
		Method to display the list of credentials saved.
		'''
		user_credentials_list = []
		for credential in cls.list_of_credentials:
			if credential.username == username:
				user_credentials_list.append(credential)
		return user_credentials_list



	@classmethod
	def find_by_credential_name(cls, credential_account):
		'''
		Method that takes in a credential_account and returns a credential that matches that credential_account.
		'''
		for credential in cls.list_of_credentials:
			if credential.credential_account == credential_account:
				return credential
		return False

	@classmethod
	def copy_credential(cls,credential_account):
		'''
		Method that copies a credential to the clipboard.
		'''
		try:
			find_credential = Credential.find_by_credential_name(credential_account)
			print(f'Your Password for {credential_account} has been copied. You can paste it anywhere now.')
			return pyperclip.copy(find_credential.password)
		
		except 	AttributeError: 
			return "Invalid credential name" 
