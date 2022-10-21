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

        # fast sign Part
        self.signInPageObj.fast_sign_in()

        self.yourProfileObj.click_in_to_account_and_lists()
        time.sleep(1)

        self.yourProfileObj.manage_your_profiles()
        self.yourProfileObj.edit_profile_neme()
        time.sleep(1)
        self.yourProfileObj.click_to_save_change_button()

        time.sleep(2)

    def tearDown(self):
        print("called tearDown")
