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
        # This method combines moving to the center of an element with pressing and releasing the left mouse button twice.
        clickable = self.driver.find_element(By.ID, "clickable")
        ActionChains(self.driver) \
            .double_click(clickable) \
            .perform()

    def click_and_hold(self):
        # This method combines moving the mouse to the center of an element with pressing the left mouse button. This is useful for focusing a specific element
        clickable = self.driver.find_element(By.ID, "clickable")
        ActionChains(self.driver) \
            .click_and_hold(clickable) \
            .perform()

    def click_and_release(self):
        # This method combines moving to the center of an element with pressing and releasing the left mouse button. This is otherwise known as “clicking”
        clickable = self.driver.find_element(By.ID, "click")
        ActionChains(self.driver) \
            .click(clickable) \
            .perform()

    def context_click(self):
        # This method combines moving to the center of an element with pressing and releasing the right mouse button (button 2). This is otherwise known as “right-clicking”
        clickable = self.driver.find_element(By.ID, "clickable")
        ActionChains(self.driver) \
            .context_click(clickable) \
            .perform()

    def move_to_element(self):
        # This method moves the mouse to the in-view center point of the element. This is otherwise known as “hovering.” Note that the element must be in the viewport or else the command will error.
        hoverable = self.driver.find_element(By.ID, "hover")
        ActionChains(self.driver) \
            .move_to_element(hoverable) \
            .perform()

    def offset_from_element(self):
        mouse_tracker = self.driver.find_element(By.ID, "mouse-tracker")
        ActionChains(self.driver) \
            .move_to_element_with_offset(mouse_tracker, 8, 0) \
            .perform()

    def drag_and_drop_on_element(self):
        # This method firstly performs a click-and-hold on the source element, moves to the location of the target element and then releases the mouse.
        draggable = self.driver.find_element(By.ID, "draggable")
        droppable = self.driver.find_element(By.ID, "droppable")
        ActionChains(self.driver) \
            .drag_and_drop(draggable, droppable) \
            .perform()

    def drag_and_drop_by_offset(self):
        # This method firstly performs a click-and-hold on the source element, moves to the given offset and then releases the mouse.
        draggable = self.driver.find_element(By.ID, "draggable")
        start = draggable.location
        finish = self.driver.find_element(By.ID, "droppable").location
        ActionChains(self.driver) \
            .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y']) \
            .perform()

    def click_to_element(self, element):
        element.click()

    def perform(self):
        element = ActionChains(self.driver)
        element.perform()

    def set_text(self, element, text):
        ellement = ActionChains(self.driver)
        ellement.send_keys_to_element(element, text)

    def get_text(self, element):
        element.text()

    def clear_text(self, element):
        element.clear()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url
