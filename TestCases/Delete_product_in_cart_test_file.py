import time
# --------------------------------------------------------------------------------------
from Src.Pages.Delete_product_in_cart_page_file import DeleteProductPageClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from TestCases.Base_test_file import BaseTestClass
from Common.Variables.Variables_file import VariablesClass


class DeleteProduct(BaseTestClass):
    def setUp(self):
        self.DeleteProductPageObj = DeleteProductPageClass(self.driver)
        self.signInPageObj = SignInPageClass(self.driver)

    def test_delete_product(self):
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

        self.DeleteProductPageObj.click_for_go_to_add_to_cart_page()
        time.sleep(2)
        # delete product in Amazon cart
        self.DeleteProductPageObj.delete_product_in_Amazon_cart()

        time.sleep(5)

    def tearDown(self):
        print("called tearDown")
