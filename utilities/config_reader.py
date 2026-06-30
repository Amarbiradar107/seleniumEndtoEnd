import configparser
from pathlib import Path


class ConfigReader:
    """
    Reads values from config.ini.
    """

    def __init__(self):
        config_path = Path(__file__).resolve().parent.parent / "config" / "config.ini"

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get(self, key):
        return self.config["DEFAULT"][key]