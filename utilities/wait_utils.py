from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:

    DEFAULT_TIMEOUT = 10

    @staticmethod
    def wait_for_clickable(driver, locator):

        return WebDriverWait(
            driver,
            WaitUtils.DEFAULT_TIMEOUT
        ).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def wait_for_visible(driver, locator):

        return WebDriverWait(
            driver,
            WaitUtils.DEFAULT_TIMEOUT
        ).until(
            EC.visibility_of_element_located(locator)
        )