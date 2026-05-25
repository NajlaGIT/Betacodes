from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import Config


def get_driver() -> webdriver.Chrome:
    """Return a configured Chrome WebDriver instance."""
    options = Options()

    if Config.HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    return driver
