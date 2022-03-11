import unittest
import aos1_locators as locators
import aos1_methods as methods

class AOSAppPositiveTestCases(unittest.TestCase):  #create class

    @staticmethod              #refers to unittest it is a static method
    def test_create():
        methods.setUp()
        methods.create_new_account()
        methods.validate_new_account()
        print(f'------ A New account is created, Username is {locators.new_user_name}')
        # Logout
        methods.logout()
        #sleep(0.5)
        # Login
        methods.login()
        # Validate New User can login (see if you can reuse New Account Validation)
        methods.validate_new_account()
        print(f'------New user {locators.new_user_name} can log in!')
        methods.logger('created')
        # Logout
        methods.logout()
        print(f'------New user {locators.new_user_name} can log out successfully!')
        # sleep(0.25)
        methods.tearDown()

# setUp()
# # Create New Account
# create_new_account()
# # Validate New Account is created
# validate_new_account()
# print(f'------New account is created, Username is {locators.new_user_name}')
# # Logout
# logout()
# sleep(0.5)
# # Login
# login()
# # Validate New User can login (see if you can reuse New Account Validation)
# validate_new_account()
# print(f'------New user {locators.new_user_name} can log in!')
# logger('created')
# # Logout
# logout()
# print(f'------New user {locators.new_user_name} can log out successfully!')
# sleep(0.25)
# tearDown()