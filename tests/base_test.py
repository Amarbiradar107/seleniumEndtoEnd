from framework.driver_manager import DriverManager


class BaseTest:
    """
    Base class for all test classes.
    """

    @property
    def driver(self):
        return DriverManager.get_driver()

    @property
    def logger(self):
        return self.context.logger

    @property
    def config(self):
        return self.context.config