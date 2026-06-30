from pathlib import Path

from utilities.datetime_utils import DateTimeUtils


class ReportService:

    def __init__(self):

        timestamp = DateTimeUtils.timestamp()

        self.execution_folder = (
            Path("reports") / timestamp
        )

        self.execution_folder.mkdir(
            parents=True,
            exist_ok=True
        )

    @property
    def html_report(self):

        return self.execution_folder / "report.html"

    @property
    def screenshots(self):

        folder = self.execution_folder / "screenshots"

        folder.mkdir(exist_ok=True)

        return folder

    @property
    def allure_results(self):

        folder = self.execution_folder / "allure-results"

        folder.mkdir(exist_ok=True)

        return folder