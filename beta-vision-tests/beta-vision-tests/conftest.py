import pytest
from utils.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    """Yield a fresh Chrome driver per test; quit on teardown."""
    drv = get_driver()
    drv.maximize_window()
    yield drv
    drv.quit()
