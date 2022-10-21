from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By


class QuantityPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = QuantityPageLocatorsClass

    def quantity_amazon_product(self):
        qtyClick = self.find.custom_find_element(self.locators.qtyClickLocator)
        qtyClick.click()

    def click_quantity_amazon_product(self):
        secondQty = self.find.custom_find_element(self.locators.secondQtyClickLocator)
        secondQty.click()


class QuantityPageLocatorsClass():
    qtyClickLocator = (By.ID, "a-autoid-0")
    secondQtyClickLocator = (By.ID, "quantity_1")
