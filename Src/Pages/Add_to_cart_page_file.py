from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By



class AddToCartPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = AddToCartPageLocatorsClass

    def click_to_add_to_cart_button(self):
        addToCartButton = self.find.custom_find_element(self.locators.addToCartButtonLocator)
        addToCartButton.click()

    def click_for_go_to_add_to_cart_page(self):
        addToCartPage = self.find.custom_find_element(self.locators.addToCartPageLocator)
        addToCartPage.click()


class AddToCartPageLocatorsClass():
    # # Add To Cart Part
    addToCartButtonLocator = (By.ID, "add-to-cart-button")

    addToCartPageLocator = (By.ID, "nav-cart-text-container")
