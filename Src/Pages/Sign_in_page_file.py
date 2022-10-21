from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By
from Common.Variables.Variables_file import VariablesClass
import time


class SignInPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = SignInPageLocatorsClass

    def fill_username_field(self, user_name=VariablesClass.get_username()):
        userNameTextBoxElement = self.find.custom_find_element(self.locators.userNameFieldLocator)
        userNameTextBoxElement.send_keys(user_name)

    def click_into_continue_button(self):
        continueButtonElement = self.find.custom_find_element(self.locators.continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password=VariablesClass.get_password()):
        passwordTextBoxElement = self.find.custom_find_element(self.locators.passwordTextFieldLocator)
        passwordTextBoxElement.send_keys(password)

    def click_into_sign_in_button(self):
        signInButtonElement = self.find.custom_find_element(self.locators.signInButtonLocator)
        signInButtonElement.click()

    def check_to_keep_me_signed_in_checkbox(self):
        keepMeSignedInElement = self.find.custom_find_element(self.locators.keepMeSignedInLocator)
        keepMeSignedInElement.click()

    def fast_sign_in(self, username=VariablesClass.get_username(), password=VariablesClass.get_password()):
        """
        Opens Amazon.com sign in page and singes in.
        We can specify a username and password, otherwise the default values will be used.
        """
        self.driver.get(VariablesClass.amazonSignInUrl)
        # username
        self.fill_username_field(username)
        time.sleep(2)  # added to not get robot check
        self.click_into_continue_button()
        # password
        self.fill_password_field(password)
        self.check_to_keep_me_signed_in_checkbox()
        time.sleep(2)  # added to not get robot check
        self.click_into_sign_in_button()


class SignInPageLocatorsClass():
    userNameFieldLocator = (By.ID, "ap_email")
    continueButtonLocator = (By.ID, "continue")
    passwordTextFieldLocator = (By.ID, "ap_password")
    signInButtonLocator = (By.ID, "signInSubmit")
    keepMeSignedInLocator = (By.NAME, "rememberMe")
