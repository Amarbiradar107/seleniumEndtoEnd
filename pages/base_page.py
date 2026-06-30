from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.wait_utils import WaitUtils

class BasePage:
    """
    Base Page containing reusable Selenium methods.
    """

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def click(self, locator):
        """Click on an element."""
        WaitUtils.wait_for_clickable(
            self.driver,
            locator
        ).click()

    def enter_text(self, locator, text):
        """Enter text into a field."""
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return text from an element."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def get_title(self):
        """Return current page title."""
        return self.driver.title

    def is_visible(self, locator):
        """Check if an element is visible."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()