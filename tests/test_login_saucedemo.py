import pytest
import allure
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.config_manager import ConfigManager

config = ConfigManager("qa")

@allure.title(
    "Verify Valid Login"
)

@allure.severity(
    allure.severity_level.CRITICAL
)


@pytest.mark.usefixtures("context")

class TestLoginPage(BaseTest):
    def test_valid_login(self):
        self.logger.info("Starting Login Test")
        login = LoginPage()
        with allure.step("Open Login Page"):
            login.open()
        with allure.step("Enter Credentials"):
            inventory = login.login(
                config.username,
                config.password
            )

        with allure.step("Verify Inventory"):
            assert inventory.get_page_title() == "Products"

        self.logger.info("Login Test Passed")
