import unittest
import aos1_locators as locators
import aos1_methods as methods


class AosAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_account():
        methods.setUp()
        methods.create_new_account()
        methods.logout()
        methods.login()
        methods.logger('created')
        methods.logout()
        methods.tearDown()




