#!/usr/bin/env python3.6
import pyperclip  #importing pyperclip for copying to clipboard
from password import User  #imporing user class
from credential import Credential #importing credential class




def create_user(fname, lname, password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname, lname, password)
	return new_user


def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name, password):
	'''
	Function that verifies the existence of the user before creating credentials
	'''
	check_user = Credential.check_user(first_name, password)
	return check_user


def generate_password():
	'''
	Function to generate a password automatically
	'''
	password_gen = Credential.generate_password()
	return password_gen

def check_existing_credential(credential_account):
    '''
    Function that check if a credential exists with that credential_account and return a Boolean
    '''
    return Credential.find_by_credential_name(credential_account)

def add_credential(username, credential_account, account_name, password):
	'''
	Function to create a new credential
	'''
	new_credential = Credential(username, credential_account, account_name, password)
	return new_credential

def create_credential(username, credential_account, account_name, password):
	'''
	Function to create a new credential
	'''
	new_credential = Credential(username, credential_account, account_name, password)
	return new_credential


def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)


def del_credential(credential_account):
    '''
    Function to delete a credential
    '''
    Credential.delete_credentials()

def display_credentials(username):
	'''
	Function to display saved credentials
	'''
	return Credential.display_credentials(username)

def find_credential(credential_account):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credential.find_by_credential_name(credential_account)

def copy_credential(credential_account):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(credential_account)


def main():
    print(' ')
    print('Hello! Welcome to Password Locker.')
 
    while True:
        print("-"*34)
        print('\n')

        print('Use these short codes: \n ca - Create an Account \n lg - Login \n ex - Exit')
        print('\n')
        short_code = input('Enter your choice: ').lower()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-"*20)
            print('\n')
            print('Create a new account:')
            print('\n')

            first_name = input('Enter your first name - ')
            last_name = input('Enter your last name - ')
            password = input('Enter your password - ')
            save_user(create_user(first_name, last_name, password))
            
            print(f'New Account Created for: {first_name} {last_name} using password: {password}')
            print('\n')

        elif short_code == 'lg':
            print("-"*20)
            print('\n')
            print('Enter your account details to login:')
            print('\n')

            username = input('Enter your first name - ')
            password = str(input('Enter your password - '))
            user_exists = verify_user(username,password)
            if user_exists == username:
                print('\n')
                print(f'Welcome {username}. Please select a short code to continue.')
                

                while True:
                    print("-"*30)
                    print('Our short codes: \n ac-Add existing Credential \n cc-Create a Credential \n sc-Display Credentials \n fc- Find a Credential  \n cp-Copy Password \n rc- Delete account \n ex-Exit' )
                    print('\n')
                    short_code = input('Enter a choice: ').lower()
                    print("-"*20)

                    if short_code == 'ex':
                        
                        print(f'Thank you for using Password Locker. Goodbye {username}')
                        print("-"*50)
                        break

                    elif short_code == 'ac':
                        print('\n')
                        print('Enter your existing credentials:')
                        print('\n')
                        username = input('Enter your username- ')
                        credential_account = input('Enter the credential account- ')
                        account_name = input('Enter your account name - ')
                        password = input('Enter your password: ')

                        save_credential(add_credential(username,credential_account,account_name,password))
                        print('\n')
                        print(f'Credential added: username: {username} credential account: {credential_account} - Account Name: {account_name} - Password: {password}')
                        print('\n')


                    elif short_code == 'cc':
                        print('\n')
                        print('Enter your new credentials:')
                        print('\n')
                        credential_account = input('Enter the credential account- ')
                        account_name = input('Enter your account name - ')

                        while True:
                            print('\n')
                            print("-"*20)
                            print('Please select an option for creating a password: \n ep - enter your password \n gp - generate a password \n ex - exit')
                            passKey = input('Enter an option: ').lower()
                            print("-"*10)

                            if passKey == 'ep':
                                print('\n')
                                password = input('Enter your password: ')
                                break
                            elif passKey == 'gp':
                                password = generate_password()
                                break
                            elif passKey == 'ex':
                                break
                            else:
                                print('Wrong option entered. Try again!')

                        save_credential(create_credential(username,credential_account,account_name,password))
                        print('\n')
                        print(f'Credential Created: credential account: {credential_account} - Account Name: {account_name} - Password: {password}')
                        print('\n')
                    
                        
    
                    elif short_code == 'fc':
                        print("Enter the credential account name you want to search for:")
    
                        credential_account = input()
                        if check_existing_credential(credential_account):
                                credential = find_credential(credential_account)
                                print(f"Here is the Credentials for {credential.credential_account} ")
                                print('\n')
                                print(f'credential account Name: {credential.credential_account} - Account Name: {credential.account_name} - Password: {credential.password}')
                                print('\n')
                                print('-' * 30)
        
                        else:
                                print('\n')
                                print("That credential does not exist")
    
                    elif short_code == 'rc':
                        print('\n')
                        print("Enter the credential account name of the credentials you want to remove")
                        print('\n')
    
                        credential_account = input('Enter the credential account name- ')
                        

                        if del_credential(credential_account):
                                credential = del_credential(credential_account)
                                credential.delete_credentials()
                                credential = del_credential(credential)
                                print("Here is a list of deleted credentials")
                                print('\n')


                        else:
                                print('\n')
                                print("That credential does not exist")
                                print('\n')

                    elif short_code == 'sc':
                        print('\n')
                        if display_credentials(username):
                            print('Here is a list of all your credentials')
                          
                            for credential in display_credentials(username):
                                print(f'credential account Name: {credential.credential_account} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print('\n')
                        else:
                            print('\n')
                            print("You don't seem to have saved any credentials yet. enter cc to create one.")
                            print('\n')

                    elif short_code == 'cp':
                       
                        credential_account = input('Enter the credential account name for the credential password to copy: ')
                        copy_credential(credential_account)
                        print('\n')
                    else:
                        print('Wrong option entered. Try again!')

            else:
                
                print('Wrong details entered. Try again or Create an Account!')

        else:
            print("-"*50)
            print('\n')
            print('Wrong option entered. Try again!')


if __name__ == '__main__':
	main()