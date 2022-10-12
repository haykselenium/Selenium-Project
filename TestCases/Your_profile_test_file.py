import time
# --------------------------------------------------------------------------------------
from Src.Pages.Account.Click_in_to_profile_page_file import YourProfilePageClass
from Src.Pages.Sign_in_page_file import SignInPageClass
from TestCases.Base_test_file import BaseTestClass
from Common.Variables.Variables_file import VariablesClass


class YourProfile(BaseTestClass):
    def setUp(self):
        self.yourProfileObj = YourProfilePageClass(self.driver)
        self.signInPageObj = SignInPageClass(self.driver)

    def test_your_profile(self):
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

        self.yourProfileObj.click_in_to_account_and_lists()
        time.sleep(3)

        self.yourProfileObj.manage_your_profiles()
        self.yourProfileObj.edit_profile_neme()
        time.sleep(2)
        self.yourProfileObj.click_to_save_change_button()

        time.sleep(5)

    def tearDown(self):
        print("called tearDown")
