from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self,driver):
        self.driver = driver

    edit_your_account_information_option_link_text = "Edit your account information"

    def display_status_of_edit_your_account_information_option(self):
        return self.driver.find_element(By.LINK_TEXT,self.edit_your_account_information_option_link_text).is_displayed()
