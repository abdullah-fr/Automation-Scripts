"""
Proper Automation Testing - Demo App
Testing a system we control = reliable, reproducible tests
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

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


# ==================== LOGIN TESTS ====================

def test_login_page_loads(driver):
    """Test 1: Login page loads successfully"""
    driver.get(f"{BASE_URL}/login")

    assert "Login" in driver.title
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()


def test_login_with_valid_credentials(driver):
    """Test 2: Login with correct credentials"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(2)

    assert "dashboard" in driver.current_url
    assert "Welcome" in driver.page_source


def test_login_with_empty_email(driver):
    """Test 3: Login fails with empty email"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(1)

    assert "login" in driver.current_url


def test_login_with_empty_password(driver):
    """Test 4: Login fails with empty password"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(1)

    assert "login" in driver.current_url


def test_login_with_wrong_password(driver):
    """Test 5: Login fails with incorrect password"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("WrongPassword123")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(1)

    assert "Invalid email or password" in driver.page_source


def test_login_with_unregistered_email(driver):
    """Test 6: Login fails with non-existent email"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "email").send_keys("nonexistent@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    time.sleep(1)

    assert "Invalid email or password" in driver.page_source


# ==================== SIGNUP TESTS ====================

def test_signup_page_loads(driver):
    """Test 7: Signup page loads successfully"""
    driver.get(f"{BASE_URL}/signup")

    assert "Sign Up" in driver.title
    assert driver.find_element(By.ID, "first_name").is_displayed()
    assert driver.find_element(By.ID, "last_name").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()


def test_signup_with_valid_data(driver):
    """Test 8: Signup with valid information"""
    driver.get(f"{BASE_URL}/signup")

    timestamp = str(int(time.time()))

    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys(f"john{timestamp}@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Test123!")
    driver.find_element(By.ID, "signup-btn").click()

    time.sleep(2)

    assert "login" in driver.current_url
    assert "Account created successfully" in driver.page_source


def test_signup_with_empty_first_name(driver):
    """Test 9: Signup fails with empty first name"""
    driver.get(f"{BASE_URL}/signup")

    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Test123!")
    driver.find_element(By.ID, "signup-btn").click()

    time.sleep(1)

    assert "signup" in driver.current_url


def test_signup_with_short_password(driver):
    """Test 10: Signup fails with password < 6 characters"""
    driver.get(f"{BASE_URL}/signup")

    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "confirm_password").send_keys("123")
    driver.find_element(By.ID, "signup-btn").click()

    time.sleep(1)

    assert "at least 6 characters" in driver.page_source


def test_signup_with_mismatched_passwords(driver):
    """Test 11: Signup fails when passwords don't match"""
    driver.get(f"{BASE_URL}/signup")

    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Different123!")
    driver.find_element(By.ID, "signup-btn").click()

    time.sleep(1)

    assert "Passwords do not match" in driver.page_source


def test_signup_with_existing_email(driver):
    """Test 12: Signup fails with already registered email"""
    driver.get(f"{BASE_URL}/signup")

    driver.find_element(By.ID, "first_name").send_keys("John")
    driver.find_element(By.ID, "last_name").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "confirm_password").send_keys("Test123!")
    driver.find_element(By.ID, "signup-btn").click()

    time.sleep(1)

    assert "Email already registered" in driver.page_source


# ==================== NAVIGATION TESTS ====================

def test_navigation_login_to_signup(driver):
    """Test 13: Navigate from login to signup page"""
    driver.get(f"{BASE_URL}/login")

    signup_link = driver.find_element(By.LINK_TEXT, "Sign up")
    signup_link.click()

    time.sleep(1)

    assert "signup" in driver.current_url


def test_navigation_signup_to_login(driver):
    """Test 14: Navigate from signup to login page"""
    driver.get(f"{BASE_URL}/signup")

    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()

    time.sleep(1)

    assert "login" in driver.current_url


# Run all tests with HTML report
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=demo_app_test_report.html", "--self-contained-html"])
