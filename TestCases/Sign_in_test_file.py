import time
import unittest
# --------------------------------------------------------------------------------------
from selenium import webdriver
from Src.Pages.Sign_in_page_file import SignInPageClass


class SgnIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../Common/Drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)

    def test_amazon_sign_in(self):
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        signInPageObj = SignInPageClass(self.driver)

        # Username Part
        signInPageObj.fill_username_field()
        signInPageObj.click_into_continue_button()

        # Password Part ------------------------
        signInPageObj.fill_password_field()
        signInPageObj.check_to_keep_me_signed_in_checkbox()
        # This Sleep Should Not Be There But We Add Because Amazon Detect That It Is a Robot
        time.sleep(6)
        signInPageObj.click_into_sign_in_button()

        # Search Part ----------------------------
        signInPageObj.fill_search_field()
        signInPageObj.product_search()

        # Add To Card Part -------------------------------
        signInPageObj.click_to_add_to_cart_button()
        signInPageObj.click_for_go_to_add_to_cart_page()

        # Delete Items On Cart Part ---------------------------
        signInPageObj.delete_products_in_Amazon_cart()
        # signInPageObj.delete_all_products_in_Amazon_cart()

        time.sleep(5)

    def tearDown(self):
        print("called tearDown")
