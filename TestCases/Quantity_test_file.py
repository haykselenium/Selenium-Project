import time
# --------------------------------------------------------------------------------------
from Src.Pages.Quantity_page_file import QuantityPageClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from Src.Pages.Main_page_file import MainPageClass
from Src.Pages.Add_to_cart_page_file import AddToCartPageClass
from TestCases.Base_test_file import BaseTestClass
from Common.Variables.Variables_file import VariablesClass


class Quantity(BaseTestClass):
    def setUp(self):
        self.QuantityPageObj = QuantityPageClass(self.driver)
        self.signInPageObj = SignInPageClass(self.driver)
        self.mainPageObj = MainPageClass(self.driver)
        self.addToCart = AddToCartPageClass(self.driver)

    def test_quantity_amazon_product(self):
        self.driver.get(VariablesClass.amazonSignInUrl)

        # Username Part
        self.signInPageObj.fill_username_field()
        self.signInPageObj.click_into_continue_button()

        # Password Part ------------------------
        self.signInPageObj.fill_password_field()
        self.signInPageObj.check_to_keep_me_signed_in_checkbox()
        # This Sleep Should Not Be There But We Add Because Amazon Detect That It Is a Robot
        time.sleep(6)
        self.signInPageObj.click_into_sign_in_button()

        # search
        self.mainPageObj.fill_search_field()
        self.mainPageObj.click_into_submit_button()
        self.mainPageObj.product_search()

        # quantity  test  -- - -- --- - -- - -- - -- - - -- - -- - -- - -
        self.QuantityPageObj.quantity_amazon_product()
        self.QuantityPageObj.click_quantity_amazon_product()

        # ------------------------------------------------------------

        self.addToCart.click_to_add_to_cart_button()

        time.sleep(5)

    def tearDown(self):
        print("called tearDown")
