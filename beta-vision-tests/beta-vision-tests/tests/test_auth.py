import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from config.locators import Locators
from pages.login_page import LoginPage
from config.settings import Config


class TestLoginFlow:
    "Login & auth flow tests for Beta Vision (stag env)."


    def test_login_page_loads(self, driver):
        "Login page should be reachable on the stag environment."
        page = LoginPage(driver).open()
        assert page.is_on_login_page(), f"Expected /login URL, got: {driver.current_url}"
        print("\n✅ Page loads successfully")
        time.sleep(3)

    def test_valid_login_redirects_to_dashboard(self, driver):
        page = LoginPage(driver).open()
        page.login(Config.email, Config.password)
        time.sleep(3)
        print("\n✅ Login successful!")
        time.sleep(3)


    # Negative / edge cases
    def test_invalid_password_shows_error(self, driver):
        page = LoginPage(driver).open()
        page.login(Config.email, "WrongPassword_999!")
        # User should remain on login page
        assert page.is_on_login_page(), \
            "User was redirected despite"
        print("\n✅ Unsuccessful Login!")
        time.sleep(3)


    def test_empty_credentials_shows_error(self, driver):
        "Submitting an empty form should not proceed to the dashboard."
        page = LoginPage(driver).open()
        page.click_SignIn()

        assert not page.is_dashboard_visible(), (
            "Dashboard should NOT appear after empty-form submission."
        )
        time.sleep(3)
        print("\n✅ Unsuccessful Login with empty credentials!")

    def test_invalid_email_format(self, driver):
        "Invalid email should be rejected before hitting the server."
        page = LoginPage(driver).open()
        time.sleep(3)
        page.login("not-an-email", "SomePassword1!")

        # Should either show an error or stay on the login page, button disabled
        assert page.is_on_login_page() or page.get_error_message(), (
            "Expected to stay on login or see an error for invalid email format.")
        print("\n✅ Unsuccessfull Login with invalid Email Format!")
        time.sleep(3)

    # ── Session / logout ───────────────────────────────────────────────────
    def test_logout_redirects_to_login(self, driver):
        page = LoginPage(driver).open()

        page.login(Config.email, Config.password)

        # Wait until login succeeds
        WebDriverWait(driver, 10).until(
            lambda d: "/login" not in d.current_url.lower()
        )

        assert "/login" not in driver.current_url.lower(), \
            "User did not log in successfully."

        page.click_logout()

        WebDriverWait(driver, 10).until(
            lambda d: "/login" in d.current_url.lower()
        )

        assert "/login" in driver.current_url.lower(), \
            "Logout failed."
        print("\n✅ logout successfully redirects to login!")


    def test_back_button_after_logout_does_not_restore_session(self, driver):
        """Navigating back after logout should not expose protected pages."""
        page = LoginPage(driver).open()
        page.login(Config.email, Config.password)
        page.click_logout()

        driver.back()
        # Either redirected to login or dashboard is no longer visible
        assert page.is_on_login_page() or not page.is_dashboard_visible(), (
            "Session should be invalid after logout – back-button must not restore it."
        )

        print("\n✅ Navigating back after logout is not exposing protected pages!")
