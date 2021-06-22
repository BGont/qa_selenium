import logging
from pathlib import Path
import pytest

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

log_dir = Path("/log")

logging.basicConfig(level=logging.INFO, filename=str(log_dir / "tests.log"),
                    format="%(asctime)s: %(levelname)s: %(name)s: %(message)s",
                    datefmt="%d-%m-%Y %I:%M:%S")


class CrashListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        driver.save_screenshot(str(log_dir / f"{driver.session_id}.png"))


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "edge"], default="chrome")
    parser.addoption("--bversion", action="store", default="90.0")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--video", action="store_true", default=False)
    parser.addoption("--url", action="store", default="https://192.168.137.1",
                     help="base URL of Opencart app")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--bversion")
    base_url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    video = request.config.getoption("--video")
    vnc = request.config.getoption("--vnc")

    capabilities = {
        "browserName": browser,
        "browserVersion": version,
        "acceptSslCerts": True,
        "acceptInsecureCerts": True,
        "selenoid:options": {
            "enableVideo": video,
            "enableVNC": vnc,
        }
    }

    executor_url = f"http://{executor}:4444/wd/hub"
    driver = EventFiringWebDriver(webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=capabilities),
        CrashListener())
    driver.url = base_url

    request.addfinalizer(driver.quit)

    return driver

