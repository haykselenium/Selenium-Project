from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By
import names
from selenium.webdriver.common.keys import Keys


class YourProfilePageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Custom_find_file.CustomFind(driver)
        self.locators = YourProfilePageLocatorsClass

    def click_in_to_account_and_lists(self):
        accountAndListsButton = self.find.custom_find_element(self.locators.accountAndListsLocator)
        accountAndListsButton.click()
        yourProfiles = self.find.custom_find_element(self.locators.yourProfilesLocator)
        yourProfiles.click()

    def manage_your_profiles(self):
        profileName = self.find.custom_find_element(self.locators.profileNameLocator)
        profileName.click()
        editName = self.find.custom_find_element(self.locators.editNameLocator)
        editName.click()
        nameTextBox = self.find.custom_find_element(self.locators.nameTextBoxLocator)
        nameTextBox.clear()
        nameText = names.get_name(gender='male')
        nameTextBox.sendKeys(nameText)


class YourProfilePageLocatorsClass():
    accountAndListsLocator = (By.ID, "nav-link-accountList-nav-line-1")
    yourProfilesLocator = (By.XPATH, "(//div[@class='a-row'])[6]")

    profileNameLocator = (By.ID, "home-profile-active")
    editNameLocator = (By.ID, "name-edit-pencil-image")

    nameTextBoxLocator = (By.ID, "profile-name-text-input")

# import java.util.UUID;
#
# String uuid = UUID.randomUUID().toString();
#
# //Now this uuid enter to your text box
# driver.findElement(By.id("text box id")).sendKeys(uuid);
