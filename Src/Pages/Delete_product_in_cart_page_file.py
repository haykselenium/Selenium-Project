from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By


class DeleteProductPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = DeleteProductPageLocatorsClass

    def click_for_go_to_add_to_cart_page(self):
        addToCartPage = self.find.custom_find_element(self.locators.addToCartPageLocator)
        addToCartPage.click()

    def delete_product_in_Amazon_cart(self):
        deleteItemInCart = self.find.custom_find_element(self.locators.deleteItemsInCartLocator)
        deleteItemInCart.click()


class DeleteProductPageLocatorsClass():
    deleteItemsInCartLocator = (By.CSS_SELECTOR, 'input[value="Delete"]')
    addToCartPageLocator = (By.ID, "nav-cart-text-container")
