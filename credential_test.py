import unittest
import pyperclip 
from credential import Credential 



class TestUser(unittest.TestCase):

    '''
    Test class that defines the test cases for the the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Setup method to run before each test case 
        ''' 
        self.new_user = User('josee', 'Mukandayisenga', 'abcdef')
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"josee")
        self.assertEqual(self.new_user.last_name,"mukandayisenga")
        self.assertEqual(self.new_user.password,"abcdef")
        
    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the users list
		'''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.users_list = []

        
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for the the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
		Setup method to run before each test case
		'''
        self.new_credential = Credential('josee','instagram','mukjos30','abcdef')

    def test__init__(self):
        '''
		Test to check if the reation of credential instances is properly done
		'''
        self.assertEqual(self.new_credential.username,'josee')
        self.assertEqual(self.new_credential.credential_account,'instagram')
        self.assertEqual(self.new_credential.account_name,'mukjos30')
        self.assertEqual(self.new_credential.password,'abcdef')
        
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credentials() # saving the new credential
        
        self.assertEqual(len(Credential.list_of_credentials),1)
        
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credential to check if we can save multiple credentials
        objects to our list_of_credentials
        '''
        self.new_credential.save_credentials()
        test_credential = Credential("jojo","social","mukjos30","abcdef") # new credential
        test_credential.save_credentials()
        
        self.assertEqual(len(Credential.list_of_credentials),2)
        
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.list_of_credentials = []
            
    def test_find_by_credential_name(self):
        '''
		Test to check if we can find a credential by credential_account
		'''
        self.new_credential.save_credentials()
        test_user = Credential('josee','tuitter','josee mukandayisenga','abcdef')
        test_user.save_credentials()
        
        credential_exists = Credential.find_by_credential_name('tuitter')
        self.assertEqual(credential_exists,test_user)
        
    def test_display_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.new_credential.save_credentials()
        test_user = Credential('josee','tuitter','josee mukandayisenga','abcdef')
        test_user.save_credentials()
        
        self.assertEqual(Credential.display_credentials(User),Credential.user_credentials_list)
        
    def test_copy_credential(self):
        '''
		Test to confirm if we can copy a credential from saved credentials
		'''
        self.new_credential.save_credentials()
        test_user = Credential('josee','tuitter','josee mukandayisenga','abcdef')
        test_user.save_credentials() 
        Credential.copy_credential('abcdef')
        
        self.assertEqual(self.new_credential.password,pyperclip.paste())
        print(pyperclip.paste())
  
        
if __name__ == '__main__':
    unittest.main()