from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SignInPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = SignInPageLocatorsClass

    def fill_username_field(self, userName="testcaseselenium123321@gmail.com"):
        userNameTextBoxElement = self.find.custom_find_element(self.locators.userNameFieldLocator)
        userNameTextBoxElement.send_keys(userName)

    def click_into_continue_button(self):
        continueButtonElement = self.find.custom_find_element(self.locators.continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password="Test123321"):
        passwordTextBoxElement = self.find.custom_find_element(self.locators.passwordTextFieldLocator)
        passwordTextBoxElement.send_keys(password)

    def click_into_sign_in_button(self):
        signInButtonElement = self.find.custom_find_element(self.locators.signInButtonLocator)
        signInButtonElement.click()

    def check_to_keep_me_signed_in_checkbox(self):
        keepMeSignedInElement = self.find.custom_find_element(self.locators.keepMeSignedInLocator)
        keepMeSignedInElement.click()

    def fill_search_field(self):
        searchTextBoxElement = self.find.custom_find_element(self.locators.searchTextFieldLocator)
        searchTextBoxElement.clear()
        searchTextBoxElement.send_keys("iphone")
        searchTextBoxElement.send_keys(Keys.ENTER)

    def product_search(self):
        searchProduct = self.find.custom_find_element(self.locators.productSearchLocator)
        searchProduct.click()

    def click_to_add_to_cart_button(self):
        addToCartButton = self.find.custom_find_element(self.locators.addToCartButtonLocator)
        addToCartButton.click()

    def click_for_go_to_add_to_cart_page(self):
        addToCartPage = self.find.custom_find_element(self.locators.addToCartPageLocator)
        addToCartPage.click()

    def delete_products_in_Amazon_cart(self):
        deleteItemsInCart = self.find.custom_find_element(self.locators.deleteItemsInCartLocator)
        deleteItemsInCart.click()

    def delete_all_products_in_Amazon_cart(self):
        deleteAllItemsInCart = self.find.custom_find_element(self.locators.deleteAllItemsInCartLocator)
        deleteAllItemsInCart.click()


class SignInPageLocatorsClass():
    # Username Part
    userNameFieldLocator = (By.ID, "ap_email")
    continueButtonLocator = (By.ID, "continue")

    # Password Part
    passwordTextFieldLocator = (By.ID, "ap_password")
    signInButtonLocator = (By.ID, "signInSubmit")
    keepMeSignedInLocator = (By.NAME, "rememberMe")

    # Search Button
    searchTextFieldLocator = (By.ID, "twotabsearchtextbox")
    # Product search Part
    productSearchLocator = (By.LINK_TEXT, "Apple iPhone 12, 128GB, White - Unlocked (Renewed Premium)")

    # Add To Cart Part
    addToCartButtonLocator = (By.ID, "add-to-cart-button")

    addToCartPageLocator = (By.ID, "nav-cart-text-container")

    deleteItemsInCartLocator = (By.NAME, "submit.delete.C2f6b182b-edf0-4276-83cc-60c0a28bc29e")

    deleteAllItemsInCartLocator = ()
