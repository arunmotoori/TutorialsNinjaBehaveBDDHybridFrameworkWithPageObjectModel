from datetime import datetime
from behave import *
from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigated to Login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.select_login_option()


@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context,email,password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    context.account_page = context.login_page.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()


@when(u'I enter invalid email and valid password say "{password}" into the fields')
def step_impl(context,password):
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@then(u'I should get a proper warning message')
def step_impl(context):
    assert context.login_page.display_status_of_warning_message("Warning: No match for E-Mail Address and/or Password.")


@when(u'I enter valid email say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context,email,password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I enter invalid email and invalid password say "{password}" into the fields')
def step_impl(context,password):
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")


