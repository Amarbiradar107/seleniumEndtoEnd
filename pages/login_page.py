from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from utilities.config_manager import ConfigManager
from utilities.config_reader import ConfigReader
from framework.driver_manager import DriverManager

class LoginPage(BasePage):
    def __init__(self):
        super().__init__(DriverManager.get_driver())

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        config = ConfigManager()
        self.driver.get(
                        config.base_url
                        )

    def login(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

        return InventoryPage(self.driver)