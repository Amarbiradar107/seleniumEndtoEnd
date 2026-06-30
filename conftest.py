import pytest

from framework.context import FrameworkContext
from framework.driver_manager import DriverManager
from utilities.browser_factory import BrowserFactory
from utilities.config_manager import ConfigManager
from utilities.screenshot import ScreenshotManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to execute tests"
    )

    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Execution environment"
    )


# @pytest.fixture(scope="function")
# def driver(request):
#     environment = request.config.getoption("--env")
#     config = ConfigManager(environment)
#     browser = request.config.getoption("--browser")
#
#     if browser is None:
#         browser = config.browser
#
#     driver = BrowserFactory.get_driver(browser)
#
#     yield driver
#
#     driver.quit()

@pytest.fixture
def context(request):

    env = request.config.getoption("--env")

    context = FrameworkContext(env)

    driver = BrowserFactory.get_driver(context.config)

    DriverManager.set_driver(driver)

    yield context

    DriverManager.quit_driver()

@pytest.fixture(autouse=True)
def inject_context(request, context):
    """
    Automatically inject FrameworkContext
    into BaseTest-derived classes.
    """

    if request.cls:
        request.cls.context = context

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        ScreenshotManager.capture(item.name)

def pytest_sessionstart(session):
    print("\n========== Test Execution Started ==========\n")


def pytest_sessionfinish(session, exitstatus):
    print("\n========== Test Execution Finished ==========\n")