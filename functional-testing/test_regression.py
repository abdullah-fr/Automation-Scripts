"""
Regression Testing Suite
Comprehensive tests to ensure no existing functionality is broken
Supports parallel execution with pytest-xdist
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
    options.add_argument('--headless')  # Run faster without UI
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


# ==================== LOGIN REGRESSION TESTS ====================

@pytest.mark.regression
@pytest.mark.login
def test_login_page_elements(driver):
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
    """Regression: Valid login works correctly"""
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
def test_login_empty_email_validation(driver):
    """Regression: Empty email validation works"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))

    assert "login" in driver.current_url


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.validation
def test_login_empty_password_validation(driver):
    """Regression: Empty password validation works"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password")))

    assert "login" in driver.current_url


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.validation
def test_login_wrong_password(driver):
    """Regression: Wrong password shows error"""
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
def test_login_unregistered_email(driver):
    """Regression: Unregistered email shows error"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "email").send_keys("nonexistent@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 10).until(
        lambda d: "Invalid email or password" in d.page_source
    )

    assert "Invalid email or password" in driver.page_source


# ==================== SIGNUP REGRESSION TESTS ====================

@pytest.mark.regression
@pytest.mark.signup
def test_signup_page_elements(driver):
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
    """Regression: Valid signup creates account"""
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
def test_signup_empty_first_name(driver):
    """Regression: Empty first name validation works"""
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
def test_signup_short_password(driver):
    """Regression: Short password validation works"""
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
def test_signup_mismatched_passwords(driver):
    """Regression: Password mismatch validation works"""
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
def test_signup_existing_email(driver):
    """Regression: Duplicate email validation works"""
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


# ==================== NAVIGATION REGRESSION TESTS ====================

@pytest.mark.regression
@pytest.mark.navigation
def test_navigation_login_to_signup(driver):
    """Regression: Navigation from login to signup works"""
    driver.get(f"{BASE_URL}/login")

    signup_link = driver.find_element(By.LINK_TEXT, "Sign up")
    signup_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains("signup"))

    assert "signup" in driver.current_url


@pytest.mark.regression
@pytest.mark.navigation
def test_navigation_signup_to_login(driver):
    """Regression: Navigation from signup to login works"""
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


# Run regression tests with parallel execution
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🔄 REGRESSION TESTING SUITE")
    print("="*60)
    print("Running comprehensive tests in parallel...")
    print("="*60 + "\n")

    pytest.main([
        __file__,
        "-v",
        "-m", "regression",
        "-n", "4",  # Run 4 tests in parallel
        "--html=regression_test_report.html",
        "--self-contained-html"
    ])
