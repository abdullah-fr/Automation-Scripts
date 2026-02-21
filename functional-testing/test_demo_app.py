"""
Comprehensive Test Suite - Demo App
Includes Smoke Tests (critical path) and Regression Tests (comprehensive)
- Smoke tests: Quick sanity checks
- Regression tests: Run in parallel with pytest-xdist
- All tests use explicit waits for professional-grade automation
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


BASE_URL = "http://localhost:5000"


@pytest.fixture
def driver():
    """Setup and teardown browser"""
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--headless')  # Run in headless mode for speed
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


# ==================== SMOKE TESTS (Critical Path) ====================

@pytest.mark.smoke
def test_app_is_running(driver):
    """Smoke Test: Verify application is accessible"""
    driver.get(BASE_URL)
    assert "Login" in driver.title or "Sign Up" in driver.title


@pytest.mark.smoke
def test_login_page_loads_smoke(driver):
    """Smoke Test: Login page loads successfully"""
    driver.get(f"{BASE_URL}/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    assert driver.find_element(By.ID, "login-btn").is_displayed()


@pytest.mark.smoke
def test_signup_page_loads_smoke(driver):
    """Smoke Test: Signup page loads successfully"""
    driver.get(f"{BASE_URL}/signup")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first_name")))
    assert driver.find_element(By.ID, "first_name").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()


@pytest.mark.smoke
def test_valid_login_works_smoke(driver):
    """Smoke Test: Valid login redirects to dashboard"""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url


@pytest.mark.smoke
def test_navigation_works_smoke(driver):
    """Smoke Test: Navigation between pages works"""
    driver.get(f"{BASE_URL}/login")
    signup_link = driver.find_element(By.LINK_TEXT, "Sign up")
    signup_link.click()
    WebDriverWait(driver, 10).until(EC.url_contains("signup"))
    assert "signup" in driver.current_url

    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()
    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    assert "login" in driver.current_url


# ==================== REGRESSION TESTS - LOGIN ====================

@pytest.mark.regression
@pytest.mark.login
def test_login_page_loads(driver):
    """Regression: Verify all login page elements are present"""
    driver.get(f"{BASE_URL}/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

    assert "Login" in driver.title
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    assert driver.find_element(By.ID, "login-btn").is_displayed()
    assert driver.find_element(By.LINK_TEXT, "Sign up").is_displayed()


@pytest.mark.regression
@pytest.mark.login
def test_login_with_valid_credentials(driver):
    """Regression: Login with correct credentials"""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url
    assert "Welcome" in driver.page_source


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.validation
def test_login_with_empty_email(driver):
    """Regression: Login fails with empty email"""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    assert "login" in driver.current_url


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.validation
def test_login_with_empty_password(driver):
    """Regression: Login fails with empty password"""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password")))
    assert "login" in driver.current_url


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.validation
def test_login_with_wrong_password(driver):
    """Regression: Login fails with incorrect password"""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("WrongPassword123")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 10).until(
        lambda d: "Invalid email or password" in d.page_source
    )
    assert "Invalid email or password" in driver.page_source


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.validation
def test_login_with_unregistered_email(driver):
    """Regression: Login fails with non-existent email"""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "email").send_keys("nonexistent@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 10).until(
        lambda d: "Invalid email or password" in d.page_source
    )
    assert "Invalid email or password" in driver.page_source


# ==================== REGRESSION TESTS - SIGNUP ====================

@pytest.mark.regression
@pytest.mark.signup
def test_signup_page_loads(driver):
    """Regression: Verify all signup page elements are present"""
    driver.get(f"{BASE_URL}/signup")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first_name")))

    assert "Sign Up" in driver.title
    assert driver.find_element(By.ID, "first_name").is_displayed()
    assert driver.find_element(By.ID, "last_name").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    assert driver.find_element(By.ID, "confirm_password").is_displayed()
    assert driver.find_element(By.ID, "signup-btn").is_displayed()


@pytest.mark.regression
@pytest.mark.signup
def test_signup_with_valid_data(driver):
    """Regression: Signup with valid information"""
    driver.get(f"{BASE_URL}/signup")
    timestamp = str(int(time.time()))

    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys(f"john{timestamp}@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Test123!")
    driver.find_element(By.ID, "signup-btn").click()

    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    WebDriverWait(driver, 5).until(
        lambda d: "Account created successfully" in d.page_source
    )
    assert "login" in driver.current_url
    assert "Account created successfully" in driver.page_source


@pytest.mark.regression
@pytest.mark.signup
@pytest.mark.validation
def test_signup_with_empty_first_name(driver):
    """Regression: Signup fails with empty first name"""
    driver.get(f"{BASE_URL}/signup")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Test123!")
    driver.find_element(By.ID, "signup-btn").click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "first_name")))
    assert "signup" in driver.current_url


@pytest.mark.regression
@pytest.mark.signup
@pytest.mark.validation
def test_signup_with_short_password(driver):
    """Regression: Signup fails with password < 6 characters"""
    driver.get(f"{BASE_URL}/signup")
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "confirm_password").send_keys("123")
    driver.find_element(By.ID, "signup-btn").click()

    WebDriverWait(driver, 10).until(
        lambda d: "at least 6 characters" in d.page_source
    )
    assert "at least 6 characters" in driver.page_source


@pytest.mark.regression
@pytest.mark.signup
@pytest.mark.validation
def test_signup_with_mismatched_passwords(driver):
    """Regression: Signup fails when passwords don't match"""
    driver.get(f"{BASE_URL}/signup")
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Different123!")
    driver.find_element(By.ID, "signup-btn").click()

    WebDriverWait(driver, 10).until(
        lambda d: "Passwords do not match" in d.page_source
    )
    assert "Passwords do not match" in driver.page_source


@pytest.mark.regression
@pytest.mark.signup
@pytest.mark.validation
def test_signup_with_existing_email(driver):
    """Regression: Signup fails with already registered email"""
    driver.get(f"{BASE_URL}/signup")
    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Test123!")
    driver.find_element(By.ID, "signup-btn").click()

    WebDriverWait(driver, 10).until(
        lambda d: "Email already registered" in d.page_source
    )
    assert "Email already registered" in driver.page_source


# ==================== REGRESSION TESTS - NAVIGATION ====================

@pytest.mark.regression
@pytest.mark.navigation
def test_navigation_login_to_signup(driver):
    """Regression: Navigate from login to signup page"""
    driver.get(f"{BASE_URL}/login")
    signup_link = driver.find_element(By.LINK_TEXT, "Sign up")
    signup_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains("signup"))
    assert "signup" in driver.current_url


@pytest.mark.regression
@pytest.mark.navigation
def test_navigation_signup_to_login(driver):
    """Regression: Navigate from signup to login page"""
    driver.get(f"{BASE_URL}/signup")
    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    assert "login" in driver.current_url


@pytest.mark.regression
@pytest.mark.navigation
def test_dashboard_accessible_after_login(driver):
    """Regression: Dashboard is accessible after successful login"""
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url
    assert "Welcome" in driver.page_source


# Run all tests with HTML report
# Smoke tests run first, then regression tests in parallel
if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 COMPREHENSIVE TEST SUITE")
    print("="*70)
    print("Running Smoke Tests + Regression Tests (parallel)")
    print("="*70 + "\n")

    pytest.main([
        __file__,
        "-v",
        "-n", "4",  # Run regression tests in parallel with 4 workers
        "--html=demo_app_test_report.html",
        "--self-contained-html"
    ])
