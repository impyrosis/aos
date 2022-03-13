import unittest
import aos_locators as locators
import aos_methods as methods


class AosAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.create_new_user()
        methods.log_out()
        methods.log_in()
        methods.logger('created')
        methods.log_out()
        methods.tearDown()
        methods.check_homepage_text()
        methods.check_shopnow_button()
        methods.check_main_menu()
        methods.check_mainlogo()
        methods.contact_us()
        methods.check_socialmedia_link()
        methods.tearDown()




