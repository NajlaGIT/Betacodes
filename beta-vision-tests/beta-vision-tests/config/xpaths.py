from selenium.webdriver.common.by import By


class XPaths:
    # Auth
    # EMAIL_INPUT = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/form/div[3]/div/input")  # update if selector differs
    SIGN_IN_BUTTON = "//button[@type='submit']"
    ERROR_MESSAGE = "//*[contains(text(),'Email or Password is not Valid')]"
    LOGOUT_BUTTON = "//*[contains(text(),'Logout Account')]"