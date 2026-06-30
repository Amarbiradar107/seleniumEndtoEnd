from selenium import webdriver
from selenium.webdriver import Remote

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from tests.test_login_saucedemo import config


class BrowserFactory:

    @staticmethod
    def get_driver(config):

        browser = config.browser.lower()
        headless = config.headless
        execution = config.execution

        # Create browser-specific options
        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")

        elif browser == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Local Execution
        if config.execution.lower() == "local":

            if browser == "chrome":
                driver = webdriver.Chrome(options=options)

            elif browser == "firefox":
                driver = webdriver.Firefox(options=options)

            elif browser == "edge":
                driver = webdriver.Edge(options=options)

        # Selenium Grid Execution
        elif config.execution.lower() == "grid":

            driver = Remote(
                command_executor=config.grid_url,
                options=options
            )

        else:
            raise ValueError("Execution mode must be either 'local' or 'grid'.")

        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver