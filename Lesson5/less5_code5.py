'''
Problem:
    Write a program that uses a dictionary that contains ten user names and passwords. 
    The program should ask the user to enter their username and password. If the username is not in the dictionary, 
    the program should indicate that the person is not a valid user of the system. If the username is in the dictionary, 
    but the user does not enter the right password, the program should say that the password is invalid. 
    If the password is correct, then the program should tell the user that they are now logged in to the system.
'''

class LogIn:
    def __init__(self):
        self.user_credentials = {
            'user1': 'password1',
            'user2': 'password2',
            'user3': 'password3',
            'user4': 'password4',
            'user5': 'password5',
            'user6': 'password6',
            'user7': 'password7',
            'user8': 'password8',
            'user9': 'password9',
            'user10': 'password10'
        }
        self.username = None # property that stores the inputted username by the user
        self.password = None # property that stores the inputted password by the user
    
    def get_user_input(self):
        print(' ----------------------------------')
        print('|                                  |')
        print('|              LOG IN              |')
        print('|                                  |')
        print(' ----------------------------------')
        self.username = input(' Enter your username: ') # Note: Username is case-sensitive. Meaning, the user input must be exactly the same as in the database/dictionary
        self.password = input(' Enter your password: ') # Note: Password is case-sensitive. Meaning, the user input must be exactly the same as in the database/dictionary
    
    def validate_password(self, password):
        # if the inputted password by the user is the same as the password stored in the dictionary, return True
        if self.password == password: 
            return True
        else:
            return False

    def validate_username(self):
        # validate if the inputted username by the user is stored in the dictionary 'user_credentials' using get() method then store in password
        password = self.user_credentials.get(self.username)
        # if the username inputted by the user is in the dictionary, validate next if the password inputted by the user is in the dictionary as well in order to log in
        if password:
            is_input_password_valid = self.validate_password(password) # store the boolean value in the is_input_password_valid
            if is_input_password_valid: # if password inputted by the user is the same as the password stored in the dictionary, display successful log in
                self.display_successful_log_in()
            else: # else if the password inputted by the user is not the same as the password stored in the dictionary, display password is invalid
                print('\n Error: Invalid password...')
        # else if the username inputted by the user is not stored in the dictionary, display that the user is not a valid user of the system
        else:
            print("\n I'm sorry. You are not a valid user of the system.")
    
    def display_successful_log_in(self):
        print('') # newline purposes
        print('\n You have successfully logged in to the system!')

class Program:
    def main(self):
        log_in = LogIn()
        log_in.get_user_input()
        log_in.validate_username()

if __name__ == "__main__":
    program = Program()
    program.main()