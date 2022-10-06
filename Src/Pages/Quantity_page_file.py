from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class QuantityPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = QuantityPageLocatorsClass

    def quantity_amazon_product(self):
        qTYqTYClick = self.find.custom_find_element(self.locators.qTYClickLocator)
        qTYqTYClick.click()


class QuantityPageLocatorsClass():
    qTYClickLocator = (By.ID, "a-autoid-0")