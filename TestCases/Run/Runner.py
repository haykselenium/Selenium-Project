from unittest import TestLoader, TestSuite, TextTestRunner
from unittest.suite import TestSuite
from TestCases.Sign_in_test_file import SignIn
from TestCases.Search_functionality_test_file import SearchFunctionality
from TestCases.Add_to_cart_test_file import AddToCart
from TestCases.Delete_product_in_cart_test_file import DeleteProduct


class RunnerClass():
    pass


if __name__ == "__main__":
    loader = TestLoader()

    suite = TestSuite((
        loader.loadTestsFromTestCase(SignIn),
        loader.loadTestsFromTestCase(SearchFunctionality),
        loader.loadTestsFromTestCase(AddToCart),
        loader.loadTestsFromTestCase(DeleteProduct)

    ))

    # run test
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

# ------------------------------------------------------------------------------------


# import unittest
#
#
# # ToDo Create Test Case that will add product to cart "Meline"
#
# # ToDo Create Test Case that will clear card all products ""
#
# class RunnerClass():
#     # Todo Organize unittest creating suite part "Nelli"
#     pass
#
#
# if __name__ == "__main__":
#     pass
#     # Todo get suite and run "Hayk"
#
#     # ToDo Generate HTML report "Vahag"
