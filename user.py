class User:
    """
    Class that generates new instances of user identify for creating an account in the app
    """
    listUser = []  
    def __init__(self, firstName, lastName, userName, passWord):

        self.fname = firstName
        self.lname = lastName
        self.uname = userName
        self.pword = passWord

 
    def saveUser(self):
        '''
        saveUser method saves user objects into userList
        '''
        User.listUser.append(self)
 
    @classmethod
    def displayUser(cls):
        '''
        method that returns the user list
        '''
        return cls.listUser

 
    @classmethod
    def findByUserName(cls, uname):
        '''
        Method that takes in a username and returns a user that matches that username.
        Args:
        number: userName to search for
        Returns :
        Identity of person that matches the userName.
        '''
        for user in cls.listUser:
            if user.uname == uname:
                return user
    @classmethod
    def findUserUname(cls, uname):
         '''
        Method that takes in a number and returns a user that matches that username.
        '''
         for user in cls.listUser:
            if user.uname == uname:
                return user.uname
    @classmethod
    def checkUname(cls, uname):
        '''
        Method that takes in a  username and returns a boolean.
        '''
        for user in cls.listUser:
            if user.uname == uname:
                return True
        return False
 
    @classmethod
    def findUserPword(cls,pword):
         '''
        Method that takes in a password and returns a user that matches that password.
        Args:
            password: password to search for
        Returns :
            user that matches the password.
        '''
         for user in cls.listUser:
            if user.pword == pword:
                return user.pword

    
    @classmethod
    def checkPWord(cls, pword):
        '''
        Method that takes in a  password and returns a boolean.
        '''
        for user in cls.listUser:
            if user.pword == pword:
                return True
        return False
