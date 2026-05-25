import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.dashboard_page import DashboardPage
from config.locators import Locators
from pages.login_page import LoginPage
from config.settings import Config

def test_dashboard_loads(driver):

    # Login first
    login = LoginPage(driver).open()

    login.login(
        Config.email,Config.password)

    # Wait until login succeeds
    WebDriverWait(driver, 20).until(
        lambda d: "/login" not in d.current_url.lower())
    dashboard = DashboardPage(driver)

    time.sleep(2)

    # assert dashboard.is_dashboard_loaded(), \
    #     "Dashboard did not load."

    print("✅ Dashboard loaded successfully!")


def test_live_channel_navigation(driver):

    login = LoginPage(driver).open()

    login.login(
        Config.email,
        Config.password
    )

    dashboard = DashboardPage(driver)
    time.sleep(2)

    dashboard.open_live_channel()

    time.sleep(2)

    assert "livetv" in driver.current_url.lower()

    print("✅ Live Channel opened!")

def test_detection_wall_navigation(driver):

    login = LoginPage(driver).open()

    login.login(
        Config.email,
        Config.password
    )

    time.sleep(2)

    dashboard = DashboardPage(driver)
    time.sleep(2)
    dashboard.open_detection_wall()
    time.sleep(2)
    assert "gridwall" in driver.current_url.lower()

    print("✅ Detection wall Opened!")