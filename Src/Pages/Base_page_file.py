from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Common.Find.Custom_find_file import CustomFind


class BasePageClass:
    def __init__(self, driver):
        self.driver = driver
        self.find = CustomFind(driver)

    def click_to_element(self, element):
        element.click()

    def double_click(self):
        clickable = self.driver.find_element(By.ID, "clickable")
        ActionChains(self.driver) \
            .double_click(clickable) \
            .perform()

    def click_and_hold(self):
        clickable = self.driver.find_element(By.ID, "clickable")
        ActionChains(self.driver) \
            .click_and_hold(clickable) \
            .perform()

    def set_text(self, settext):
        return self.find.custom_find_element(settext)

    def get_text(self, text):
        return self.find.custom_find_element(text)

    def clear_text(self):
        return self.driver.clear

    def find_element(self, locator):
        return self.find.custom_find_element(locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url
