from Common.Find import Custom_find_file
from selenium.webdriver.common.by import By
import names


# from selenium.webdriver.common.keys import Keys


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
        manageYourProfile = self.find.custom_find_element(self.locators.manageYourProfileLocator)
        manageYourProfile.click()
        profileNameClick = self.find.custom_find_element(self.locators.profileNameLocator)
        profileNameClick.click()

    def edit_profile_neme(self):
        nameTextBox = self.find.custom_find_element(self.locators.nameTextBoxLocator)
        nameTextBox.clear()
        rand_name = names.get_full_name(gender='male')
        nameTextBox.send_keys(rand_name)

    def click_to_save_change_button(self):
        saveChange = self.find.custom_find_element(self.locators.saveChangeLocator)
        saveChange.click()


class YourProfilePageLocatorsClass():
    accountAndListsLocator = (By.ID, "nav-link-accountList-nav-line-1")
    yourProfilesLocator = (By.XPATH, "(//div[@class='a-row'])[6]")

    manageYourProfileLocator = (By.CSS_SELECTOR, 'p.a-spacing-mini')
    profileNameLocator = (By.ID, "name-edit-modal-link")

    nameTextBoxLocator = (By.ID, "profile-name-text-input")
    saveChangeLocator = (By.CSS_SELECTOR, "span#profile-name-edit-submit-button")
