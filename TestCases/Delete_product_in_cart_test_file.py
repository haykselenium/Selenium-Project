import time
# --------------------------------------------------------------------------------------
from Src.Pages.Delete_product_in_cart_page_file import DeleteProductPageClass
from TestCases.Base_test_file import BaseTestClass


class SignIn(BaseTestClass):
    def setUp(self):
        self.DeleteProductPageObj = DeleteProductPageClass(self.driver)

    def test_amazon_sign_in(self):
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        self.DeleteProductPageObj.delete_product_in_Amazon_cart()

        time.sleep(5)

    def tearDown(self):
        print("called tearDown")
