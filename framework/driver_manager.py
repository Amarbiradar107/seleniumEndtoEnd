from selenium.webdriver.remote.webdriver import WebDriver


class DriverManager:
    """
    Stores the current WebDriver instance.
    """

    _driver: WebDriver | None = None

    @classmethod
    def set_driver(cls, driver: WebDriver) -> None:
        cls._driver = driver

    @classmethod
    def get_driver(cls) -> WebDriver:
        if cls._driver is None:
            raise RuntimeError("Driver has not been initialized.")
        return cls._driver

    @classmethod
    def quit_driver(cls) -> None:
        if cls._driver:
            cls._driver.quit()
            cls._driver = None