from datetime import datetime


class DateTimeUtils:

    @staticmethod
    def timestamp():

        return datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )