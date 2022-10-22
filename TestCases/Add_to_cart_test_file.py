import time

from TestCases.Base_test_file import BaseTestClass
from Src.Pages.Add_to_cart_page_file import AddToCartPageClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from Common.Variables.Variables_file import VariablesClass
from Src.Pages.Main_page_file import MainPageClass


class AddToCart(BaseTestClass):
    def setUp(self):
        self.addToCartPageObj = AddToCartPageClass(self.driver)
        self.signInPageObj = SignInPageClass(self.driver)
        self.mainPageObj = MainPageClass(self.driver)

    def test_add_to_cart(self):
        self.driver.get(VariablesClass.amazonSignInUrl)

        # fast sign Part
        self.signInPageObj.fast_sign_in()

        # product search part
        self.mainPageObj.fill_search_field()
        self.mainPageObj.click_into_submit_button()
        self.mainPageObj.product_search()

        self.addToCartPageObj.click_to_add_to_cart_button()

        time.sleep(1)
    def tearDown(self):
        print("called tearDown")
