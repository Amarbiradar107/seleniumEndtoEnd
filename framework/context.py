from framework.logger_manager import LoggerManager
from utilities.config_manager import ConfigManager


class FrameworkContext:

    def __init__(self, environment="qa"):

        self.config = ConfigManager(environment)

        self.logger = LoggerManager.get_logger("Framework")