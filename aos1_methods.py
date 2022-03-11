# AOS methods for Capstone Project

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.support.select import Select
import aos1_locators as locators
import sys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome(
    executable_path="C:\\Users\\RAO\\PycharmProjects\\pythonProject\\aos\\chromedriver.exe")


def setUp():
    # 2. Maximize the browser window.
    driver.maximize_window()
    driver.implicitly_wait(30)
    # 3. Navigate to web page URL - https://advantageonlineshopping.com/ (Links to an external site.)
    driver.get(locators.home_page_url)
    print(f'{driver.current_url}')  # Tip: Use print(driver.current_url) to find the actual AOS Website URL
    print(f'{driver.title}')  # Tip: Use print(driver.title) to find the actual title.

    # 4. Check URL and home page title are as expected.
    if driver.current_url == locators.home_page_url and driver.title == locators.home_page_title:
        print(f'{locators.home_page_url} Hurray launched successfully!')
        # print(f'The actual AOS website URL is {driver.current_url} and the actual title is {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.home_page_url} Sorry did not launch.Please check the code or website')
        print(f'Current URL is {driver.current_url}. Page title is {driver.title}')
        sleep(0.25)
        tearDown()


def tearDown():
    if driver is not None:
        print('---------------------~*~---------------------')
        print(f'########### The test is completed at {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# 5. Create Selenium Automated Scripts that will do the following
# Create New Account - using Faker library fake data
def create_new_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.5)
    # assert driver.find_element((By.ID,'registerPage')).is_displayed()
    # sleep(0.25)

    for i in range(len(locators.list_opt)):
        if locators.list_names[i]:
            driver.find_element(By.NAME, locators.list_names[i]).send_keys(locators.list_val[i])
            sleep(0.25)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)


# Validate New Account is created
def validate_new_account():
    # Validate New Account created (new username is displayed in the top menu)
    if driver.title == locators.home_page_title:
        sleep(0.25)
        assert driver.find_element(By.LINK_TEXT, locators.new_user_name).is_displayed()
        sleep(0.25)


def logout():
    # #Logout
    driver.find_element(By.LINK_TEXT, locators.new_user_name).click()
    # driver.find_element(By.XPATH, f'//@id="menuUserLink"/span[contains(.,"{new_user_name}")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    # driver.find_element(By.ID,'hrefUserIcon').click()
    # java_script=driver.find_element(By.XPATH,'//label[contains(.,Sign out")]')
    # driver.execute_script("argument[0].click()",java_script)
    # 6. Close the browser and display user-friendly messages.


# 1.  Add Login functionality
def login():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    assert driver.find_element(By.XPATH, '//button[contains(.,"SIGN IN")]').is_displayed()
    sleep(0.5)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_user_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"SIGN IN")]').click()
    sleep(0.25)


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('AOSmessage.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.new_email}\t'
          f'{locators.new_user_name}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


setUp()
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
