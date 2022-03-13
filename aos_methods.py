import sys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

import aos_locators
import aos_locators as locators
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
    # driver.implicitly_wait(30)
    # 2. Maximize the browser window.
    driver.maximize_window()
    driver.implicitly_wait(30)
    # time.sleep(.3)
    # 3. Navigate to web page URL - https://advantageonlineshopping.com/ (Links to an external site.)

    driver.get(locators.aos_url)
    time.sleep(2)
    # 4. Check URL and home page title are as expected.
    print(driver.current_url)  # current URL
    print(driver.title)
    if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
        print(f' The URL is : {driver.current_url} and title of webpage is :{driver.title}')
        sleep(0.25)
    else:
        print(f' Ooops something went wrong. Please check URL of page again!')
        sleep(0.25)
        # tearDown()


def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        time.sleep(2)
        driver.close()
        driver.quit()


# Create New Account - using Faker library fake data
def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    time.sleep(2)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    time.sleep(2)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.new_email)
    time.sleep(2)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    time.sleep(2)
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
    time.sleep(2)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    time.sleep(2)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    time.sleep(2)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
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
    print(f' the registered  username is  : "{locators.new_username}" and password is: "{locators.new_password}"')
    # logger('created')


# Validate New Account is created

def validate_new_account():
    # Validate New Account created (new username is displayed in the top menu)
    if driver.title == locators.aos_home_page_title:
        sleep(0.25)
        assert driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed()
        sleep(0.25)


# Logout
def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    print('---------------*%*----------------')
    print(f'The {driver.current_url} was closed at: {datetime.datetime.now()}')
    # driver.close()
    # driver.quit()


# login
def log_in():
    print('*************log in funcationality********************')
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="hrefUserIcon"]').click()
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(0.30)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print('Logged in as: ', locators.new_username)
    sleep(0.25)

    #
    #
    #
    #
    # #
    # # if driver.current_url == locators.aos_url and driver.title == locators.aos_home_page_title:
    # #     print(f' The URL is : {driver.current_url} and the title of the web-page is :{driver.title}')
    # # else:
    # #     print(f' Something went wrong. Please Check URL of the web page!')
    # # time.sleep(2)
    # driver.find_element(By.ID, 'menuUser').click()
    # time.sleep(2)
    # assert driver.find_element(By.XPATH, '//button[contains(.,"SIGN IN")]').is_displayed()
    # time.sleep(2)
    # driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    # time.sleep(2)
    # driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    # time.sleep(3)
    # driver.find_element(By.ID, 'sign_in_btnundefined').click()
    # time.sleep(4)
    # # CHECK-LOGIN
    # # x = driver.find_element(By.XPATH,
    # #                         f'//*[@id="menuUser"]/span[contains(.,"{locators.new_username}")]').is_displayed()
    # # print(x)
    # if x == True:
    #     print(f' Hurray login was successful')
    # else:
    #     print(f' Sorry problem found - help needed ')


# logger
def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.new_email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


def check_homepage_text():
    if driver.title == locators.aos_home_page_title:
        sleep(0.25)
        for i in range(len(locators.homepage_texts)):
            if locators.homepage_textid[i]:
                assert driver.find_element(By.ID, locators.homepage_textid[i]).is_displayed()
                sleep(0.25)

        # assert driver.find_element(By.ID,'speakersTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'laptopsTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'miceTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'headphonesTxt').is_displayed()
        # sleep(0.25)
        print('Homepage texts are displayed!')


def check_shopnow_button():
    if driver.title == locators.aos_home_page_title:
        sleep(0.25)
        for i in range(len(locators.homepage_texts)):
            driver.find_element(By.ID, locators.homepage_textid[i]).click()
            sleep(0.25)
            path = locators.homepage_texts[i]

            # print(f'{path}')
            # assert driver.find_element(By.XPATH,'f//h3[contains(text(),"{path}")]').is_displayed()
            sleep(0.5)
            driver.find_element(By.XPATH, '//a[contains(text(),"HOME")]').click()
            sleep(0.25)
            # driver.get(locators.home_page_url)
            # sleep(0.25)
        print('Shop Now button are clickable')
        sleep(0.25)


def check_main_menu():
    if driver.title == locators.aos_home_page_title:
        # for i in range(len(locators.homepage_menu)):
        # b = driver.find_element(By.XPATH, f'//a[contains(text(),{locators.homepage_menu[i]})]')
        b = driver.find_element(By.XPATH, "//a[contains(text(),'SPECIAL OFFER')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu SPECIAL OFFER is clickable')
        sleep(0.25)
        b = driver.find_element(By.XPATH, "//a[contains(text(),'POPULAR ITEMS')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu POPULAR ITEMS is clickable')
        sleep(0.25)
        b = driver.find_element(By.XPATH, "//a[contains(text(),'CONTACT US')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu CONTACT US is clickable')
        sleep(0.25)

    print('menu item are clickable')


def check_mainlogo():
    if driver.title == locators.aos_home_page_title:
        sleep(0.25)
        assert driver.find_element(By.XPATH, '//span[contains(text(),"dvantage")]').is_displayed()
        print('Main logo is displayed')


def check_socialmedia_link():
    driver.get(locators.aos_url)
    if driver.title == locators.aos_home_page_title:
        sleep(0.25)
        driver.find_element(By.NAME, 'follow_facebook').click()
        sleep(0.25)
        driver.switch_to.window(driver.window_handles[1])
        # print(f'{driver.current_url}')
        if driver.current_url == locators.fb_page_url:
            sleep(0.25)
            print("Facebook links on Homepage is clickable")
            sleep(0.25)
            driver.close()

    driver.switch_to.window(driver.window_handles[0])
    if driver.title == locators.aos_home_page_title:
        sleep(0.25)
        driver.find_element(By.NAME, 'follow_twitter').click()
        sleep(0.25)
        driver.switch_to.window(driver.window_handles[1])
    # print(f'{driver.current_url}')
    if driver.current_url == locators.tw_page_url:
        sleep(0.25)
        print("Twitter links on Homepage is clickable")
        sleep(0.25)
        driver.close()

    driver.switch_to.window(driver.window_handles[0])
    if driver.title == locators.aos_home_page_title:
        sleep(0.25)
        driver.find_element(By.NAME, 'follow_linkedin').click()
        sleep(0.25)
    driver.switch_to.window(driver.window_handles[1])
    # print(f'{driver.current_url}')
    # if driver.current_url == locators.in_page_url:
    sleep(0.25)
    print("LinkedIn links on Homepage is clickable")
    sleep(0.25)
    # driver.close()
    sleep(0.25)


# driver.switch_to.window(driver.window_handles[0])


def contact_us():
    sleep(0.25)
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Headphones')
    sleep(0.25)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('HP H2310 In-ear Headset')
    sleep(0.25)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.new_email)
    sleep(0.25)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(0.25)
    driver.find_element(By.ID, 'send_btnundefined').click()
    assert driver.find_element(By.XPATH, '//p[contains(text(),"Thank you for contacting Advantage support.")]')
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'CONTINUE SHOPPING').click()
    if driver.current_url == locators.aos_url:
        print('CONTACT US form is working properly')


def check_homepage():
    # setUp()
    check_homepage_text()
    sleep(0.25)
    check_shopnow_button()
    sleep(0.25)
    check_main_menu()
    sleep(0.25)
    check_mainlogo()
    sleep(0.25)
    contact_us()
    sleep(0.25)
    check_socialmedia_link()
    sleep(0.25)


def delete_account():
    if driver.current_url == locators.aos_url:
        log_in()
        validate_new_account()
        driver.find_element(By.LINK_TEXT, locators.new_username).click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH, "//label[contains(text(),'- No orders -')]").is_displayed()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, locators.new_username).click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My account")]').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH, f'//label[contains(.,"{locators.account_first_name}")]').is_displayed()
        sleep(0.25)
        assert driver.find_element(By.XPATH, f'//label[contains(.,"{locators.account_last_name}")]').is_displayed()
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[contains(text(),"Delete Account")]').click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[contains(text(),"yes")]').click()
        sleep(0.5)
        log_in()
        assert driver.find_element(By.XPATH,'//label[contains(.,"Incorrect user name or password.")]').is_displayed()
        sleep(0.25)
        print(f'{locators.new_username} account is deleted')
        logger('deleted')


setUp()
# create_new_user()
check_shopnow_button()
check_main_menu()
contact_us()
check_homepage()
check_socialmedia_link()
# tearDown()
# log_out()
# validate_new_account()
# print(f'------New account is created, Username is {locators.new_username}')
# sleep(0.5)
#     log_in()
#     create_new_user()
#     validate_new_account()
#     delete_account()
# print(f'------New user {locators.new_username} can log in!')
# logger('created')
#     log_out()
# print(f'------New user {locators.new_username} can log out successfully!')
# sleep(0.25)
tearDown()

#
# setUp()
# create_new_user()
# check_shopnow_button()
# log_in()
# check_main_menu()
# contact_us()
# check_homepage_text()
# tearDown()
# # create_new_user()
# # log_out()
# delete_account()
# validate_new_account()
# log_out()
# # log_in()
# logger('created')
# sleep(0.25)
# tearDown()
