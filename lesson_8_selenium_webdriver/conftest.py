from pathlib import Path
import pytest
import os

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "edge"], default="chrome")
    parser.addoption("--dir", action="store", default="d:\\services\\webdrivers",
                     help="Path to directory where webdrivers stored")
    parser.addoption("--url", action="store", default="http://127.0.0.1",
                     help="base URL of Opencart app")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    drivers_dir = request.config.getoption("--dir")
    base_url = request.config.getoption("--url")

    if browser == "chrome":
        executable_path = Path(drivers_dir) / "chromedriver" if os.name != 'nt' else Path(
            drivers_dir) / "chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.headless = headless
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Chrome(
            options=options,
            executable_path=str(executable_path)
        )
    elif browser == "firefox":
        executable_path = Path(drivers_dir) / "geckodriver" if os.name != 'nt' else Path(
            drivers_dir) / "geckodriver.exe"

        options = webdriver.FirefoxOptions()
        options.headless = headless
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = webdriver.Firefox(
            options=options,
            executable_path=str(executable_path)
        )
    elif browser == "edge" and os.name == 'nt':
        from msedge.selenium_tools import Edge, EdgeOptions
        executable_path = Path(drivers_dir) / "msedgedriver.exe"

        options = EdgeOptions()
        options.use_chromium = True
        options.headless = headless
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')

        driver = Edge(
            options=options,
            executable_path=str(executable_path)
        )
    else:
        raise ValueError("Driver not supported: {}".format(browser))

    if maximized:
        driver.maximize_window()

    driver.url = base_url

    request.addfinalizer(driver.quit)

    return driver

