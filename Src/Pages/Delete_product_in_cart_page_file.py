from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DeleteProductPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = DeleteProductPageLocatorsClass

    def delete_product_in_Amazon_cart(self):
        deleteItemInCart = self.find.custom_find_element(self.locators.deleteItemsInCartLocator)
        deleteItemInCart.click()


class DeleteProductPageLocatorsClass():
    deleteItemsInCartLocator = (By.CSS_SELECTOR, 'input[value="Delete"]')
