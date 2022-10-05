import unittest
from unittest.suite import TestSuite
from selenium import webdriver
# first test class
class TestBing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')
        print("Browser Opened in first class")
    def test_open_bing(self):
        self.driver.get("https://bing.com")
        print("bing opened")
# second test class
class TestCherCherTech(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')
        print("Browser Opened in second class")
    def test_open_bing(self):
        self.driver.get("https://chercher.tech")
        print("Chercher tech opened")
# ------------------------------------------------------------------------------------
if __name__ == "__main__":

	# create the suite from the test classes
    suite = TestSuite()
    # load the tests
    tests = unittest.TestLoader()

	# add the tests to the suite
    suite.addTests(tests.loadTestsFromTestCase(TestBing))
    suite.addTests(tests.loadTestsFromTestCase(TestCherCherTech))

    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)


#------------------------------------------------------------------------------------




















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
