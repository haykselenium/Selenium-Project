from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By


# from selenium.webdriver.common.keys import Keys


class DeleteAllProductPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = DeleteProductPageLocatorsClass

    def click_for_go_to_add_to_cart_page(self):
        addToCartPage = self.find.custom_find_element(self.locators.addToCartPageLocator)
        addToCartPage.click()

    def delete_all_product_in_Amazon_cart(self):
        while True:
            try:
                deleteAllItemInCart = self.find.custom_find_element(self.locators.deleteAllItemsInCartLocator)
                deleteAllItemInCart.click()

            except:
                break


class DeleteProductPageLocatorsClass():
    deleteAllItemsInCartLocator = (By.CSS_SELECTOR, 'input[value="Delete"]')
    addToCartPageLocator = (By.ID, "nav-cart-text-container")
    productCountLocator = (By.CSS_SELECTOR, "span#nav-cart-count")
