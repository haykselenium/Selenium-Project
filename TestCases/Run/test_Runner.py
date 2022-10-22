from unittest import TestLoader, TextTestRunner, TestSuite
from TestCases.Sign_in_test_file import SignIn
from TestCases.Search_functionality_test_file import SearchFunctionality
from TestCases.Add_to_cart_test_file import AddToCart
from TestCases.Delete_product_in_cart_test_file import DeleteProduct
from TestCases.Quantity_test_file import Quantity
from TestCases.Your_profile_test_file import YourProfile
from TestCases.Delete_all_product_in_cart_test_file import DeleteAllProduct
from TestCases.Base_test_file import BaseTestClass


class RunnerClass(BaseTestClass):
    pass


if __name__ == "__main__":
    loader = TestLoader()

    suite = TestSuite((
        # test for go to amazon cart and delete first product in cart
        loader.loadTestsFromTestCase(DeleteProduct),
        # test for SearchFunctionality in amazon
        loader.loadTestsFromTestCase(SearchFunctionality),
        # test for add product in amazon cart
        loader.loadTestsFromTestCase(AddToCart),
        # test for signin
        loader.loadTestsFromTestCase(SignIn),
        # test for product qty
        loader.loadTestsFromTestCase(Quantity),
        # test for go to profile page and change profile name
        loader.loadTestsFromTestCase(YourProfile),
        # test for go to amazon cart and delete all product in cart
        loader.loadTestsFromTestCase(DeleteAllProduct)
    ))
    # run test
    runner = TextTestRunner(verbosity=1)  # Test one by one
    # runner = TextTestRunner(verbosity=2)  # Test all in one time
    runner.run(suite)
