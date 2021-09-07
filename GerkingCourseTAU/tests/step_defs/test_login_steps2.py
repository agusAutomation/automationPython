import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from Udemy.Pages.IndexPage import IndexPage
from Udemy.Pages.LoginPage import LoginPage
from Udemy.Pages.MyAccountPage import MyAccountPage

# Constants
STORE_HOME = 'https://automationteststore.com/'

# Scenarios
scenarios('../features/Login.feature')

# Fixtures
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps
@given('the Store webPage')
def go_login_page(browser):
    browser.get(STORE_HOME)

@when(parsers.parse('complete "{user}" and "{password}"'))
def complete_user_pass(browser, user, password):
    index_page = IndexPage(browser)
    login_page = LoginPage(browser)
    ##USE PAGE OBJECT
    index_page.goToLoginPage(browser)
    #browser.find_element_by_css_selector('#customer_menu_top > li').click()
    browser.implicitly_wait(100)
    login_page.login(user, password)
    #browser.find_element_by_id('loginFrm_loginname').send_keys(user)
    #browser.find_element_by_id('loginFrm_password').send_keys(password)
    #browser.find_element_by_css_selector('button[title="Login"]').click()

@then("Login correctly")
def check_title(browser):
    assert browser.find_element_by_css_selector('h1 span.maintext').text == 'MY ACCOUNT'

@then("Error in Login")
def check_error_title(browser):
    assert 'Error: Incorrect login or password provided.' in browser.find_element_by_css_selector('div.alert-error').text