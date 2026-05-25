from selenium.webdriver.common.by import By

from config import xpaths
from config.ids import IDs
from config.xpaths import XPaths
# from config.css_selector import CSSSelectors




class Locators:

    # By Ids
    EMAIL_INPUT = (By.ID, IDs.EMAIL_INPUT)
    PASSWORD_INPUT = (By.ID, IDs.PASSWORD_INPUT)


    # By Xpaths
    SignIn_BUTTON = (By.XPATH, XPaths.SIGN_IN_BUTTON)
    ERROR_MESSAGE = (By.XPATH, XPaths.ERROR_MESSAGE)
    LOGOUT_BUTTON = (By.XPATH,XPaths.LOGOUT_BUTTON)
    # By css_selectors
    # ERROR_MESSAGE = (By.CSS_SELECTOR, CSSSelectors.ERROR_MESSAGE)
    # LOGOUT_BUTTON = (By.CSS_SELECTOR, CSSSelectors.LOGOUT_BUTTON)