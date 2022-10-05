import time

from TestCases.Base_test_file import BaseTestClass
from Src.Pages.Add_to_cart_page_file import AddToCartPageClass
from Src.Pages.Main_page_file import MainPageClass


class AddToCart(BaseTestClass):
    def setUp(self):
        self.addToCartPageObj = AddToCartPageClass(self.driver)
        self.mainPageObj = MainPageClass(self.driver)


    def add_to_cart(self):
        self.driver.get("https://www.amazon.com")

        self.mainPageObj.product_search()

        # Add To Card Part
        self.addToCartPageObj.click_to_add_to_cart_button()
        self.addToCartPageObj.click_for_go_to_add_to_cart_page()

        time.sleep(5)

    def tearDown(self):
        print("called tearDown")
