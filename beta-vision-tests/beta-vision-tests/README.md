# Beta Vision — Selenium Auth Tests (sstag env)

Pytest + Selenium Chrome test suite for login & auth flows on the **sstag** staging environment.

---

## Project structure

```
beta-vision-tests/
├── config/
│   └── settings.py        # Loads .env into a typed Config object
├── pages/
│   └── login_page.py      # Page Object for the login / auth UI
├── tests/
│   └── test_auth.py        # All login & session test cases
├── utils/
│   └── driver_factory.py  # Chrome WebDriver factory
├── conftest.py             # Shared pytest fixtures
├── pytest.ini              # Pytest configuration
├── requirements.txt
└── .env.example            # Copy → .env and fill in real values
```

---

## Setup

```bash
# 1. Clone and enter the repo
git clone <your-repo-url>
cd beta-vision-tests

# 2. Create a virtual environment (PyCharm can do this automatically)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env — set BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD
```

---

## Running tests

```bash
# All tests
pytest

# Only auth tests
pytest tests/test_auth.py -v

# Headless (CI)
HEADLESS=true pytest

# Parallel (4 workers)
pytest -n 4
```

An HTML report is written to `reports/report.html` after each run.

---

## Updating locators

All selectors live in `pages/login_page.py` under the `# Locators` section.  
Update `EMAIL_INPUT`, `PASSWORD_INPUT`, `LOGIN_BUTTON`, `DASHBOARD_INDICATOR`, etc. to match your actual sstag DOM.
