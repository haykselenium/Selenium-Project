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
    pass


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
