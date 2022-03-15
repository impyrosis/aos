from faker import Faker
fake = Faker(locale='en_CA')
#---------------------------------------------------------
app = 'Advantage online shopping'
aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = '\xa0Advantage Shopping'
# aos_login_page_url = 'https://advantageonlineshopping.com/#/'
# aos_login_page_title = '${nbsp}Advantage Shopping :Log in to the site'
aos_create_new_user = 'https://advantageonlineshopping.com/#/register'
speakers_url = 'https://advantageonlineshopping.com/#/category/Speakers/4'
tablet_url = 'https://advantageonlineshopping.com/#/category/Tablets/3'
laptop_url = 'https://advantageonlineshopping.com/#/category/Laptops/1'
mice_url = 'https://advantageonlineshopping.com/#/category/Mice/5'
headphone_url= 'https://advantageonlineshopping.com/#/category/Headphones/2'
see_offer_url = 'https://advantageonlineshopping.com/#/product/3'
explore_now_url = 'https://advantageonlineshopping.com/#/category/Tablets/3'
product_1 = 'id="16"'
product_2 = 'id="17"'
product_3 = 'id="18"'
chat_url = 'https://advantageonlineshopping.com/chat.html'
fb_link = 'https://www.facebook.com/MicroFocus/'
twitter_link = 'https://twitter.com/MicroFocus'
linkedin_link = 'https://www.linkedin.com/company/micro-focus-software?trk=tyah&trkInfo=clickedVertical%3Ashowcase%2CclickedEntityId%3A1024%2Cidx%3A2-1-2%2CtarId%3A145431482.327%2Ctas%3Ahewlett%20packard%20enterprise%20software'
headphone = 'Beats Studio 2 Over-Ear Matte Black Headphones' # product details
total_value = 'roboto-medium ng-binding'


# admin_username = 'first_name'
# admin_password = 'last_name'
# aos_dashboard_url =
# aos_dashboard_page_title =
# aos_add_new_user_page_title =
# ------------------------Fake date section------------------------------
first_name = fake.first_name()[:8]
last_name = fake.last_name()[:8]
middle_name = fake.first_name()
# full_name = f'{first_name} {last_name} {{fake.pyint(11,2999)}}'
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
phone_number = fake.phone_number()[:5]
country = fake.current_country()[:5]
city = fake.city()[:5]
address = fake.address().replace("\n", " ")[:10]  # '123 langara'
state = 'BC'  # fake.state()[:5]
postal_code = 'L6Y555'  # fake.postal_code()[:5]
creditcard = fake.phone_number()[:5] #fake.pyint(11,2999)()[:5]
cvv = '895'

# ------------------------------------------------------------------------
list_list = ['new_username', 'email', 'new_password', 'first_name', 'last_name', 'phone_number', 'country',
             'city', 'address', 'state', 'postal_code', 'new_username', 'phone_number', 'country', 'city', 'address',
             'state', 'postal_code']

list_name = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage',
             'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage', 'countryListboxRegisterPage'
    , 'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage', 'postal_codeRegisterPage']
