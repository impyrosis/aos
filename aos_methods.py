import sys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import aos1_locators as locators
from selenium.webdriver.chrome.service import Service
import time
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

print('---------------*%*----------------')
print('---------------*%*----------------')

driver: WebDriver = webdriver.Chrome(executable_path='C:\\Users\\RAO\\PycharmProjects\\pythonProject\\aos'
                                                     '\\chromedriver.exe')


def setUp():
    print(f'The testing started at: {datetime.datetime.now()}')
    print('---------------*%*----------------')
    print(f'Chrome web browser  is opened')
    driver.implicitly_wait(30)
    # 2. Maximize the browser window.
    driver.maximize_window()
    time.sleep(.3)
    # 3. Navigate to web page URL - https://advantageonlineshopping.com/ (Links to an external site.)
    driver.get(locators.home_page_url)
    time.sleep(2)
    # 4. Check URL and home page title are as expected.
    print(driver.current_url)
    print(driver.title)
    if driver.current_url == locators.home_page_url and driver.title == locators.home_page_title:
        print(f' The URL is : {driver.current_url} and the title of the web-page is :{driver.title}')
    else:
        print(f' Something went wrong. Check the URL of the web page!')


def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        time.sleep(2)
        driver.close()
        driver.quit()


# Create New Account - using Faker library fake data
def create_new_user():
    driver.find_element(By.ID, 'menuUserLink').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_user_name)
    time.sleep(.3)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.new_email)
    time.sleep(.3)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(.3)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(2)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    time.sleep(2)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    time.sleep(2)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    time.sleep(2)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    time.sleep(2)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    # SOMETIMES NUMMBER OF CHARACTER ARE EXCEED THE LIMITATION-SHOULD CORRECT IT
    # time.sleep(2)
    # driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    # time.sleep(2)
    # driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.city)
    time.sleep(2)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    time.sleep(2)
    x = driver.find_element(By.NAME, 'i_agree').is_selected()
    if x == False:
        driver.find_element(By.NAME, 'i_agree').click()
    else:
        print('there is a problem in registering')
        driver.close()
    time.sleep(5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    time.sleep(2)
    print(f' the registered  username is  : "{locators.new_user_name}" and password is: "{locators.new_password}"')
    # logger('created')


# Logout
def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    print('---------------*%*----------------')
    print(f'The {driver.current_url} was closed at: {datetime.datetime.now()}')
    # driver.close()
    # driver.quit()


# login
def log_in():
    if driver.current_url == locators.home_page_url and driver.title == locators.home_page_title:
        print(f' The URL is : {driver.current_url} and the title of the web-page is :{driver.title}')
    else:
        print(f' Something went wrong. Please Check URL of the web page!')
    time.sleep(2)
    driver.find_element(By.ID, 'menuUser').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_user_name)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    time.sleep(.3)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    time.sleep(4)
    # CHECK-LOGIN
    x = driver.find_element(By.XPATH,
                            f'//*[@id="menuUserLink"]/span[contains(.,"{locators.new_user_name}")]').is_displayed()
    print(x)
    if x == True:
        print(f' Hurray login was successful')
    else:
        print(f' Sorry problem found - help needed ')


# logger
def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.new_email}\t'
          f'{locators.new_user_name}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


setUp()
create_new_user()
log_out()
log_in()
logger('created')
tearDown()
