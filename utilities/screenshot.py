from pathlib import Path

from framework.driver_manager import DriverManager
from utilities.datetime_utils import DateTimeUtils


class ScreenshotManager:

    SCREENSHOT_DIR = Path("screenshots")

    @classmethod
    def capture(cls, name):

        cls.SCREENSHOT_DIR.mkdir(
            exist_ok=True
        )

        filename = (
            cls.SCREENSHOT_DIR /
            f"{name}_{DateTimeUtils.timestamp()}.png"
        )


        DriverManager.get_driver().save_screenshot(
            str(filename)
        )

        return filename