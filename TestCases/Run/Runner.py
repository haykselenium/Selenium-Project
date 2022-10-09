from unittest import TestLoader, TextTestRunner, TestSuite
# import time
# from unittest.suite import TestSuite
from TestCases.Sign_in_test_file import SignIn
from TestCases.Search_functionality_test_file import SearchFunctionality
from TestCases.Add_to_cart_test_file import AddToCart
from TestCases.Delete_product_in_cart_test_file import DeleteProduct
from TestCases.Quantity_test_file import Quantity
from TestCases.Your_profile_test_file import YourProfile
from TestCases.Delete_all_product_in_cart_test_file import DeleteAllProduct
import unittest
from selenium import webdriver
from TestCases.Base_test_file import BaseTestClass


class RunnerClass(BaseTestClass):
    def setUp(self):
        # navigate to the application home page
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")

        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

        # get the list of elements which are displayed after the search
        # currently on result page usingfind_elements_by_class_namemethod

        lists = self.driver.find_elements_by_class_name("r")
        no = len(lists)
        self.assertEqual(11, len(lists))

    def tearDown(self):
        # close the browser window
        self.driver.quit()



if __name__ == "__main__":
    loader = TestLoader()

    suite = TestSuite((
        # test 1
        loader.loadTestsFromTestCase(SignIn),
        # test 2
        loader.loadTestsFromTestCase(SearchFunctionality),
        # test 3
        loader.loadTestsFromTestCase(AddToCart),
        # test 4
        loader.loadTestsFromTestCase(DeleteProduct),
        # test 5
        loader.loadTestsFromTestCase(Quantity),
        # test 6
        loader.loadTestsFromTestCase(YourProfile),
        # test 7
        loader.loadTestsFromTestCase(DeleteAllProduct)
    ))

    # run test
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
