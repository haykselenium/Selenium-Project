import time
# --------------------------------------------------------------------------------------
from Src.Pages.Delete_all_product_in_cart_page_file import DeleteAllProductPageClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from TestCases.Base_test_file import BaseTestClass


class DeleteAllProduct(BaseTestClass):
    def setUp(self):
        self.DeleteAllProductPageObj = DeleteAllProductPageClass(self.driver)
        self.signInPageObj = SignInPageClass(self.driver)

    def test_delete_product(self):
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

        self.DeleteAllProductPageObj.click_for_go_to_add_to_cart_page()
        time.sleep(2)
        # delete product in Amazon cart
        self.DeleteAllProductPageObj.delete_all_product_in_Amazon_cart()

        time.sleep(5)

    def tearDown(self):
        print("called tearDown")
