from configparser import ConfigParser
from pathlib import Path


class ConfigManager:
    """
    Reads configuration for a selected environment.
    """
    _instance = None

    def __new__(cls, environment="qa"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, environment="qa"):

        config = ConfigParser()

        file = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "config"
            / "environments"
            / f"{environment}.ini"
        )

        if not file.exists():
            raise FileNotFoundError(
                f"{environment}.ini not found"
            )

        config.read(file)

        self.base_url = config["APP"]["base_url"]

        self.browser = config["BROWSER"]["browser"]

        self.headless = config.getboolean(
            "BROWSER",
            "headless"
        )

        self.timeout = config.getint(
            "BROWSER",
            "timeout"
        )

        self.username = config["CREDENTIALS"]["username"]

        self.password = config["CREDENTIALS"]["password"]

        self.execution = config["GRID"]["execution"]

        self.grid_url = config["GRID"]["grid_url"]

        self.platform = config["GRID"]["platform"]

        self.browser_version = config["GRID"]["browser_version"]