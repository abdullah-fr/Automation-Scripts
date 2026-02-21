"""
Smoke Testing Suite
Quick sanity checks to verify critical functionality works
Run these tests first before detailed regression testing
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "http://localhost:5000"


@pytest.fixture
def driver():
    """Setup and teardown browser"""
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--headless')  # Run faster without UI

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.mark.smoke
def test_app_is_running(driver):
    """Smoke Test 1: Verify application is accessible"""
    driver.get(BASE_URL)

    # Should load without errors
    assert "Login" in driver.title or "Sign Up" in driver.title


@pytest.mark.smoke
def test_login_page_loads(driver):
    """Smoke Test 2: Login page loads successfully"""
    driver.get(f"{BASE_URL}/login")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    assert driver.find_element(By.ID, "login-btn").is_displayed()


@pytest.mark.smoke
def test_signup_page_loads(driver):
    """Smoke Test 3: Signup page loads successfully"""
    driver.get(f"{BASE_URL}/signup")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first_name")))

    assert driver.find_element(By.ID, "first_name").is_displayed()
    assert driver.find_element(By.ID, "email").is_displayed()


@pytest.mark.smoke
def test_valid_login_works(driver):
    """Smoke Test 4: Valid login redirects to dashboard"""
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test123!")
    driver.find_element(By.ID, "login-btn").click()

    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    assert "dashboard" in driver.current_url


@pytest.mark.smoke
def test_navigation_works(driver):
    """Smoke Test 5: Navigation between pages works"""
    driver.get(f"{BASE_URL}/login")

    # Navigate to signup
    signup_link = driver.find_element(By.LINK_TEXT, "Sign up")
    signup_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains("signup"))
    assert "signup" in driver.current_url

    # Navigate back to login
    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains("login"))
    assert "login" in driver.current_url


# Run smoke tests
if __name__ == "__main__":
    print("\n" + "="*60)
    print("🔥 SMOKE TESTING SUITE")
    print("="*60)
    print("Running critical path tests...")
    print("="*60 + "\n")

    pytest.main([
        __file__,
        "-v",
        "-m", "smoke",
        "--html=smoke_test_report.html",
        "--self-contained-html"
    ])
