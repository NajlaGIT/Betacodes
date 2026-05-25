import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL: str           = os.getenv("BASE_URL", "http://staging.forvision.io")
    email: str         = os.getenv("TEST_USER_EMAIL", "najla@betacodespk.com")
    password: str      = os.getenv("TEST_USER_PASSWORD", "Aa123456789@@@")
    HEADLESS: bool          = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT: int      = int(os.getenv("IMPLICIT_WAIT", 20))
    PAGE_LOAD_TIMEOUT: int  = int(os.getenv("PAGE_LOAD_TIMEOUT", 30))
