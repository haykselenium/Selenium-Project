from selenium.webdriver.common.by import By
from Common.Find import Custom_find_file




class MouseActionsPageClass():
    def Click_and_hold(self):
        clickable = self.driver.find_element(By.ID, "clickable")
        ActionChains(self.driver) \
            .click_and_hold(clickable) \
            .perform()
    def Click_and_release(self):
        clickable = driver.find_element(By.ID, "click")
        ActionChains(driver) \
            .click(clickable) \
            .perform()
    def Context_Click(self):
        clickable = driver.find_element(By.ID, "clickable")
        ActionChains(driver) \
            .context_click(clickable) \
            .perform()
    def Back_Click(self):
        action = ActionBuilder(driver)
        action.pointer_action.pointer_down(MouseButton.BACK)
        action.pointer_action.pointer_up(MouseButton.BACK)
        action.perform()
    def Forward_Click(self):
        action = ActionBuilder(driver)
        action.pointer_action.pointer_down(MouseButton.FORWARD)
        action.pointer_action.pointer_up(MouseButton.FORWARD)
        action.perform()
    def Double_click(self):
        clickable = driver.find_element(By.ID, "clickable")
        ActionChains(driver) \
            .double_click(clickable) \
            .perform()
    def Move_to_element(self):
        hoverable = driver.find_element(By.ID, "hover")
        ActionChains(driver) \
            .move_to_element(hoverable) \
            .perform()
    def Move_by_offset(self):
        mouse_tracker = driver.find_element(By.ID, "mouse-tracker")
        ActionChains(driver) \
            .move_to_element_with_offset(mouse_tracker, 8, 0) \
            .perform()
    def Offset_from_Viewport(self):
        action = ActionBuilder(driver)
        action.pointer_action.move_to_location(8, 0)
        action.perform()
    def Offset_from_Current_Pointer_Location(self):
        ActionChains(driver) \
            .move_by_offset(13, 15) \
            .perform()
    def Drag_and_Drop_on_Element(self):
        draggable = driver.find_element(By.ID, "draggable")
        droppable = driver.find_element(By.ID, "droppable")
        ActionChains(driver) \
            .drag_and_drop(draggable, droppable) \
            .perform()
    def Drag_and_Drop_by_Offset(self):
        draggable = driver.find_element(By.ID, "draggable")
        start = draggable.location
        finish = driver.find_element(By.ID, "droppable").location
        ActionChains(driver) \
            .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y']) \
            .perform()