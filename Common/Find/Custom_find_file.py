from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomFind():
    def __init__(self, driver):
        self.driver = driver

    def custom_find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            print("ERROR 3: Element Not Found Exception")
            print(e)
            exit(3)
