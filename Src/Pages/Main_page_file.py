from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By


class MainPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = MainPageLocatorsClass

    def fill_search_field(self, text="iphone"):
        searchTextBoxElement = self.find.custom_find_element(self.locators.searchTextFieldLocator)
        searchTextBoxElement.clear()
        searchTextBoxElement.send_keys(text)

    def click_into_submit_button(self):
        submitButtonElement = self.find.custom_find_element(self.locators.submitButtonFieldLocator)
        submitButtonElement.click()

    def product_search(self):
        searchProduct = self.find.custom_find_element(self.locators.productSearchLocator)
        searchProduct.click()


class MainPageLocatorsClass():
    searchTextFieldLocator = (By.ID, "twotabsearchtextbox")
    submitButtonFieldLocator = (By.ID, "nav-search-submit-button")

    productSearchLocator = (By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"][1]')
