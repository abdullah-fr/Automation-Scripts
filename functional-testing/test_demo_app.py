"""
Comprehensive Test Suite - Demo App
Includes Smoke Tests (critical path) and Regression Tests (comprehensive)
- Smoke tests: Quick sanity checks
- Regression tests: Run in parallel with pytest-xdist
- Data-driven tests: Using @pytest.mark.parametrize for multiple test data
- All tests use explicit waits for professional-grade automation
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


BASE_URL = "http://localhost:5000"


# ==================== TEST DATA ====================

# Invalid login test data
INVALID_LOGIN_DATA = [
    ("", "", "empty_both"),
    ("test@example.com", "", "empty_password"),
    ("", "Test123!", "empty_email"),
    ("invalid-email", "Test123!", "invalid_email_format"),
    ("test@example.com", "wrong", "wrong_password"),
    ("test@example.com", "WrongPass123", "incorrect_password"),
    ("nonexistent@example.com", "Test123!", "unregistered_email"),
    ("test@", "Test123!", "incomplete_email"),
    ("@example.com", "Test123!", "missing_username"),
    ("test.example.com", "Test123!", "missing_at_symbol"),
]

# Invalid signup test data
INVALID_SIGNUP_DATA = [
    ("", "Doe", "john@example.com", "Test123!", "Test123!", "empty_first_name"),
    ("John", "", "john@example.com", "Test123!", "Test123!", "empty_last_name"),
    ("John", "Doe", "", "Test123!", "Test123!", "empty_email"),
    ("John", "Doe", "john@example.com", "", "Test123!", "empty_password"),
    ("John", "Doe", "john@example.com", "Test123!", "", "empty_confirm_password"),
    ("John", "Doe", "invalid-email", "Test123!", "Test123!", "invalid_email_format"),
    ("John", "Doe", "john@example.com", "123", "123", "short_password"),
    ("John", "Doe", "john@example.com", "12345", "12345", "password_5_chars"),
    ("John", "Doe", "john@example.com", "Test123!", "Different123!", "password_mismatch"),
    ("John", "Doe", "john@example.com", "Test123!", "test123!", "password_case_mismatch"),
    ("John", "Doe", "test@example.com", "Test123!", "Test123!", "existing_email"),
]

# Valid signup test data
VALID_SIGNUP_DATA = [
    ("Alice", "Smith", "Password123!", "valid_user_1"),
    ("Bob", "Johnson", "SecurePass456!", "valid_user_2"),
    ("Charlie", "Brown", "MyPass789!", "valid_user_3"),
    ("Diana", "Prince", "Wonder@123", "valid_user_4"),
    ("Eve", "Anderson", "Secure#Pass1", "valid_user_5"),
]

# Password validation test data
PASSWORD_VALIDATION_DATA = [
    ("1", "too_short_1_char"),
    ("12", "too_short_2_chars"),
    ("123", "too_short_3_chars"),
    ("1234", "too_short_4_chars"),
    ("12345", "too_short_5_chars"),
]

# Email format validation test data
EMAIL_FORMAT_DATA = [
    ("plaintext", "no_at_symbol"),
    ("@example.com", "missing_username"),
    ("user@", "missing_domain"),
    ("user@domain", "missing_tld"),
    ("user name@example.com", "space_in_username"),
    ("user@domain .com", "space_in_domain"),
]


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


# ==================== DATA-DRIVEN TESTS - LOGIN ====================

@pytest.mark.regression
@pytest.mark.login
@pytest.mark.datadriven
@pytest.mark.parametrize("email,password,test_case", INVALID_LOGIN_DATA)
def test_login_with_invalid_data(driver, email, password, test_case):
    """Data-Driven: Test login with various invalid inputs"""
    driver.get(f"{BASE_URL}/login")

    if email:
        driver.find_element(By.ID, "email").send_keys(email)
    if password:
        driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "login-btn").click()

    # Should stay on login page or show error
    WebDriverWait(driver, 5).until(
        lambda d: "login" in d.current_url or "Invalid" in d.page_source
    )

    # Verify we didn't reach dashboard
    assert "dashboard" not in driver.current_url, f"Login should fail for {test_case}"


# ==================== DATA-DRIVEN TESTS - SIGNUP ====================

@pytest.mark.regression
@pytest.mark.signup
@pytest.mark.datadriven
@pytest.mark.parametrize("first_name,last_name,email,password,confirm_password,test_case", INVALID_SIGNUP_DATA)
def test_signup_with_invalid_data(driver, first_name, last_name, email, password, confirm_password, test_case):
    """Data-Driven: Test signup with various invalid inputs"""
    driver.get(f"{BASE_URL}/signup")

    if first_name:
        driver.find_element(By.ID, "first_name").send_keys(first_name)
    if last_name:
        driver.find_element(By.ID, "last_name").send_keys(last_name)
    if email:
        driver.find_element(By.ID, "email").send_keys(email)
    if password:
        driver.find_element(By.ID, "password").send_keys(password)
    if confirm_password:
        driver.find_element(By.ID, "confirm_password").send_keys(confirm_password)

    driver.find_element(By.ID, "signup-btn").click()

    # Should stay on signup page or show error
    WebDriverWait(driver, 10).until(
        lambda d: "signup" in d.current_url or "already registered" in d.page_source.lower()
        or "do not match" in d.page_source.lower() or "at least 6" in d.page_source.lower()
    )

    # Verify we didn't reach login page with success
    if "login" in driver.current_url:
        assert "Account created successfully" not in driver.page_source, f"Signup should fail for {test_case}"


@pytest.mark.regression
@pytest.mark.signup
@pytest.mark.datadriven
@pytest.mark.parametrize("first_name,last_name,password,test_case", VALID_SIGNUP_DATA)
def test_signup_with_valid_data_multiple(driver, first_name, last_name, password, test_case):
    """Data-Driven: Test signup with multiple valid user data"""
    driver.get(f"{BASE_URL}/signup")

    timestamp = str(int(time.time() * 1000))  # More unique timestamp
    email = f"{first_name.lower()}.{last_name.lower()}.{timestamp}@example.com"

    driver.find_element(By.ID, "first_name").send_keys(first_name)
    driver.find_element(By.ID, "last_name").send_keys(last_name)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "confirm_password").send_keys(password)
    driver.find_element(By.ID, "signup-btn").click()

    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    WebDriverWait(driver, 5).until(
        lambda d: "Account created successfully" in d.page_source
    )

    assert "login" in driver.current_url, f"Signup should succeed for {test_case}"
    assert "Account created successfully" in driver.page_source


@pytest.mark.regression
@pytest.mark.signup
@pytest.mark.datadriven
@pytest.mark.validation
@pytest.mark.parametrize("password,test_case", PASSWORD_VALIDATION_DATA)
def test_signup_password_length_validation(driver, password, test_case):
    """Data-Driven: Test password length validation with various short passwords"""
    driver.get(f"{BASE_URL}/signup")

    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "confirm_password").send_keys(password)
    driver.find_element(By.ID, "signup-btn").click()

    WebDriverWait(driver, 10).until(
        lambda d: "at least 6 characters" in d.page_source
    )

    assert "at least 6 characters" in driver.page_source, f"Should show error for {test_case}"


@pytest.mark.regression
@pytest.mark.signup
@pytest.mark.datadriven
@pytest.mark.validation
@pytest.mark.parametrize("email,test_case", EMAIL_FORMAT_DATA)
def test_signup_email_format_validation(driver, email, test_case):
    """Data-Driven: Test email format validation with various invalid formats"""
    driver.get(f"{BASE_URL}/signup")

    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Test123!")
    driver.find_element(By.ID, "signup-btn").click()

    # Should stay on signup page (HTML5 validation or server-side)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))

    assert "signup" in driver.current_url, f"Should reject invalid email for {test_case}"


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
