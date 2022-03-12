from faker import Faker

fake = Faker(locale='en_CA')

# ------------------ %&%-------------------------------

aos_url = 'https://advantageonlineshopping.com/#/'
aos_home_page_title = '\xa0Advantage Shopping'

# -------------------- data section ---------------------------------
new_username = 'Re' + fake.last_name()
new_password = fake.password()
new_email = fake.email()
print(new_username, new_password, new_email)
first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()
country = fake.current_country()
city = fake.city()
address = fake.address().replace("\n", " ")
province = fake.province()
postalcode = fake.postcode()

# Print list of varaiables

# print(list_val)
homepage_texts = ['SPEAKER', 'TABLES', 'LAPTOPS', 'MICE', 'HEADPHONES']
homepage_textid = ['speakersTxt', 'tabletsTxt', 'laptopsTxt', 'miceTxt', 'headphonesTxt']
homepage_menu = ['SPECIAL OFFER', 'POPULAR ITEMS', 'CONTACT US']
fb_page_url = 'https://www.facebook.com/MicroFocus/'
tw_page_url = 'https://twitter.com/MicroFocus'
in_page_url = 'https://www.linkedin.com/company/unavailable/'

# ------------------ %&%-------------------------------
print(new_username, new_password, new_email)


# fake.pystr(min_chars=None, max_chars=10)
# middle_name = fake.first_name()
# full_name = f'{first_name} {last_name}'
# new_username = f'{first_name}{last_name}'.lower()
# new_password = fake.password()
# email = f'{new_username}@{fake.free_email_domain()}'
# email1 = fake.email()
# moodle_net_profile = f'https://moodle.net/{new_username}'
# city = fake.city()
# country = fake.current_country()
# description = f'User added by {admin_username} via \nPython Selenium Automated Script' #fake.sentence(nb_words=100) #
# pic_desc = f'pic submited by {full_name}'
# list_of_interests = [fake.job(), fake.job(), fake.job(), fake.job(), fake.job()]
# web_page = fake.url()
# icq_num = fake.pyint(111111,999999)
# skype_id = new_username
# aim_id = f'{last_name.lower()}{fake.pyint(11,9999)}'
# yahoo_id = new_username
# msn_id = f'{last_name.lower()}{fake.pyint(11,99)}{country}'
# id_num = fake.pyint(1111111,9999999)
# institution = fake.company()
# department = fake.catch_phrase()
# phone = fake.phone_number()
# mobile_phone = fake.phone_number()
# address = fake.address().replace("\n"," ")
