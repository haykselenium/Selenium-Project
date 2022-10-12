from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By


class DeleteAllProductPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = DeleteProductPageLocatorsClass

    def get_cart_products_quantity(self):
        cartButtonElement = self.find.custom_find_element(self.locators.cartButtonLocator)
        return int(cartButtonElement.text)

    def click_for_go_to_add_to_cart_page(self):
        addToCartPage = self.find.custom_find_element(self.locators.addToCartPageLocator)
        addToCartPage.click()

    def delete_all_product_in_Amazon_cart(self):
        while self.get_cart_products_quantity() > 0:
            deleteItemInCart = self.find.custom_find_element(self.locators.deleteAllItemsInCartLocator)
            deleteItemInCart.click()


class DeleteProductPageLocatorsClass():
    deleteAllItemsInCartLocator = (By.CSS_SELECTOR, 'input[value="Delete"]')
    addToCartPageLocator = (By.ID, "nav-cart-text-container")
    cartButtonLocator = (By.ID, "nav-cart-count")
