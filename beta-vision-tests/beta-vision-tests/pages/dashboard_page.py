from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.locators import Locators


class DashboardPage:
    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def is_dashboard_loaded(self):

        try:

            self.wait.until(
                EC.visibility_of_element_located(
                    Locators.Dashboard_Header
                )
            )

            return True

        except:
            return False


    def open_engagement_page(self):

        self.wait.until(EC.presence_of_element_located(Locators.Engagement_Dashboard)).click()

    def open_live_channel(self):

        self.wait.until(
            EC.element_to_be_clickable(Locators.Live_channel_link)).click()

    def open_detection_wall(self):
        self.wait.until(EC.element_to_be_clickable(Locators.Open_detection_wall)).click()
