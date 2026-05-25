import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from config.settings import Config
from config.locators import Locators

class LoginPage:
    "Page Object for the Beta Vision login / auth flow."

    # Selector that proves we are on the post-login dashboard
    # DASHBOARD_INDICATOR = (By.CSS_SELECTOR, "[data-testid='dashboard-root']")

    def __init__(self, driver: WebDriver):
        self.driver  = driver
        self.wait    = WebDriverWait(driver, Config.IMPLICIT_WAIT)

    # Actions
    def open(self) -> "LoginPage":
        self.driver.get(f"{Config.BASE_URL}/login")
        return self
    time.sleep(3)

    def enter_email(self, email: str) -> "LoginPage":
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        return self

    def click_SignIn(self) -> "LoginPage":
        self.driver.find_element(*Locators.SignIn_BUTTON).click()
        return self

    def login(self, email: str, password: str) -> "LoginPage":
        self.enter_email(email)
        self.enter_password(password)
        self.click_SignIn()
        return self


    def is_dashboard_visible(self) -> bool:
        try:
            # waits up to 20 seconds for dashboard to appear
            WebDriverWait(self.driver, 20).until(
                EC.url_changes(f"{Config.BASE_URL}/login")
            )
            time.sleep(2)  # ← extra buffer for dashboard to fully render
            return "/login" not in self.driver.current_url
        except Exception:
            return False

    def click_logout(self) -> "LoginPage":

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                Locators.LOGOUT_BUTTON
            )
        )

        logout_btn = self.driver.find_element(
            *Locators.LOGOUT_BUTTON
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout_btn
        )

        return self


    # ── Assertions / state helpers ─────────────────────────────────────────
    def is_dashboard_visible(self) -> bool:
        current_url = self.driver.current_url.lower()

        print("Dashboard Check URL:", current_url)

        return "/login" not in current_url

    def get_error_message(self) -> str:
        try:
            el = self.wait.until(
                EC.visibility_of_element_located(
                    Locators.ERROR_MESSAGE
                )
            )
            return el.text.strip()
        except Exception as e:
            print("Error message not found:", e)
            return ""

    def is_on_login_page(self) -> bool:
        return "/login" in self.driver.current_url.lower()

    # def is_dashboard_visible(self) -> bool:
    #     current_url = self.driver.current_url.lower()
    #
    #     print("Dashboard URL:", current_url)
    #
    #     return "/login" not in current_url
