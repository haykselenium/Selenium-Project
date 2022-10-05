import time
import unittest
# --------------------------------------------------------------------------------------
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Src.Pages.Sign_in_page_file import SignInPageClass
from TestCases.Base_test_file import BaseTestClass


class SgnIn(BaseTestClass):
    def setUp(self):
        self.signInPageObj = SignInPageClass(self.driver)

    def test_amazon_sign_in(self):
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        # Username Part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()

        # Password Part ------------------------
        self.signInPageObj.fill_password_field()
        self.signInPageObj.check_to_keep_me_signed_in_checkbox()
        # This Sleep Should Not Be There But We Add Because Amazon Detect That It Is a Robot
        time.sleep(6)
        self.signInPageObj.click_into_sign_in_button()

        # Search Part ----------------------------
        # self.signInPageObj.fill_search_field()
        self.signInPageObj.product_search()

        # Add To Card Part -------------------------------
        self.signInPageObj.click_to_add_to_cart_button()
        # signInPageObj.click_for_go_to_add_to_cart_page()

        # Delete Items On Cart Part ---------------------------
        # signInPageObj.delete_products_in_Amazon_cart()
        self.signInPageObj.delete_all_products_in_Amazon_cart()

        time.sleep(5)

    def tearDown(self):
        print("called tearDown")
