# Import required libraries
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup and teardown browser for each test
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


# Test 1: Navigate to Brave Search
def test_navigate_to_brave_search(driver):
    driver.get("https://search.brave.com/")
    assert "brave.com" in driver.current_url


# Test 2: Check if search box exists
def test_search_box_exists(driver):
    driver.get("https://search.brave.com/")
    wait = WebDriverWait(driver, 10)

    search_box = wait.until(EC.presence_of_element_located((By.ID, "searchbox")))
    assert search_box is not None


# Test 3: Check if search box accepts input
def test_search_box_is_interactable(driver):
    driver.get("https://search.brave.com/")
    wait = WebDriverWait(driver, 10)

    search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchbox")))
    search_box.send_keys("upwork login")

    entered_text = search_box.get_attribute("value")
    assert "upwork login" in entered_text


# Test 4: Check if search button exists
def test_search_button_exists(driver):
    driver.get("https://search.brave.com/")
    wait = WebDriverWait(driver, 10)

    search_button = wait.until(EC.presence_of_element_located((By.ID, "submit-llm-button")))
    assert search_button is not None


# Test 5: Complete search flow from start to finish
def test_complete_search_flow(driver):
    driver.get("https://search.brave.com/")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchbox")))
    search_box.send_keys("upwork login")

    search_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-llm-button")))
    search_button.click()

    wait.until(lambda d: d.current_url != "https://search.brave.com/")
    assert driver.current_url != "https://search.brave.com/"


# Run tests when file is executed directly
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
