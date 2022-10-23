import time
import unittest
from Src.Pages.Main_page_file import MainPageClass
from TestCases.Base_test_file import BaseTestClass


class SearchFunctionality(BaseTestClass):
    def setUp(self):
        self.mainPageObj = MainPageClass(self.driver)

    def test_amazon_sign_in(self):
        self.driver.get("https://www.amazon.com")
        self.assertIn("Amazon.com. Spend less. Smile more.", self.driver.title)

        # search functionality test part
        self.mainPageObj.fill_search_field()
        self.mainPageObj.click_into_submit_button()

        time.sleep(1)

    def tearDown(self):
        self.driver.close()
        print("called tearDown")


if __name__ == "__main__":
    unittest.main()
