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

        # fast sign Part
        self.signInPageObj.fast_sign_in()

        self.DeleteProductPageObj.click_for_go_to_add_to_cart_page()
        time.sleep(1)
        # delete product in Amazon cart
        self.DeleteProductPageObj.delete_product_in_Amazon_cart()

        time.sleep(1)

    def tearDown(self):
        print("called tearDown")
