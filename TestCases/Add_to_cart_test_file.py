import time

from TestCases.Base_test_file import BaseTestClass
from Src.Pages.Add_to_cart_page_file import AddToCartPageClass


class AddToCart(BaseTestClass):
    def setUp(self):
        self.addToCartPageObj = AddToCartPageClass(self.driver)

    def test_add_to_cart(self):
        self.driver.get(
            "https://www.amazon.com/ecobee-SmartThermostat-Voice-Control-Black/dp/B07NQT85FC/ref=sr_1_1_sspa?crid=1F48UXPJJD2VT&keywords=gadgets&qid=1665085678&qu=eyJxc2MiOiI5Ljk1IiwicXNhIjoiOS45MiIsInFzcCI6IjkuNDMifQ%3D%3D&sprefix=%2Caps%2C1795&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0hONlpDOUUzNDJRJmVuY3J5cHRlZElkPUEwMTk0MTEzM1FLMTIyN1cyTFBCRyZlbmNyeXB0ZWRBZElkPUEwMDA2NjM4MllKT0RPV1RTSDZORSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")

        self.addToCartPageObj.click_to_add_to_cart_button()

        # self.addToCartPageObj.click_for_go_to_add_to_cart_page()

        time.sleep(6)

    def tearDown(self):
        print("called tearDown")
