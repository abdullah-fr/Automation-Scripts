# Brave Search Automation Test Suite - Without Pytest
# Manual test execution with try/except blocks and result tracking

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup browser driver
def setup_driver():
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


# Test 1: Navigate to Brave Search
def test_navigate_to_brave_search(driver):
    try:
        driver.get("https://search.brave.com/")
        assert "brave.com" in driver.current_url
        print("✓ Test 1 PASSED: Navigate to Brave Search")
        return True
    except Exception as e:
        print(f"✗ Test 1 FAILED: {str(e)}")
        return False


# Test 2: Check if search box exists
def test_search_box_exists(driver):
    try:
        driver.get("https://search.brave.com/")
        wait = WebDriverWait(driver, 10)

        search_box = wait.until(EC.presence_of_element_located((By.ID, "searchbox")))
        assert search_box is not None
        print("✓ Test 2 PASSED: Search box exists")
        return True
    except Exception as e:
        print(f"✗ Test 2 FAILED: {str(e)}")
        return False


# Test 3: Check if search box accepts input
def test_search_box_is_interactable(driver):
    try:
        driver.get("https://search.brave.com/")
        wait = WebDriverWait(driver, 10)

        search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchbox")))
        search_box.send_keys("upwork login")

        entered_text = search_box.get_attribute("value")
        assert "upwork login" in entered_text
        print("✓ Test 3 PASSED: Search box is interactable")
        return True
    except Exception as e:
        print(f"✗ Test 3 FAILED: {str(e)}")
        return False


# Test 4: Check if search button exists
def test_search_button_exists(driver):
    try:
        driver.get("https://search.brave.com/")
        wait = WebDriverWait(driver, 10)

        search_button = wait.until(EC.presence_of_element_located((By.ID, "submit-llm-button")))
        assert search_button is not None
        print("✓ Test 4 PASSED: Search button exists")
        return True
    except Exception as e:
        print(f"✗ Test 4 FAILED: {str(e)}")
        return False


# Test 5: Complete search flow
def test_complete_search_flow(driver):
    try:
        driver.get("https://search.brave.com/")

        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchbox")))
        search_box.send_keys("upwork login")

        search_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-llm-button")))
        search_button.click()

        wait.until(lambda d: d.current_url != "https://search.brave.com/")
        assert driver.current_url != "https://search.brave.com/"
        print("✓ Test 5 PASSED: Complete search flow")
        return True
    except Exception as e:
        print(f"✗ Test 5 FAILED: {str(e)}")
        return False


# Main execution
if __name__ == "__main__":
    print("\n" + "="*50)
    print("    BRAVE SEARCH AUTOMATION TEST SUITE")
    print("="*50 + "\n")

    driver = None
    test_results = []

    try:
        # Setup browser
        driver = setup_driver()
        print("Browser launched successfully\n")

        # Run all tests and collect results
        test_results.append(test_navigate_to_brave_search(driver))
        test_results.append(test_search_box_exists(driver))
        test_results.append(test_search_box_is_interactable(driver))
        test_results.append(test_search_button_exists(driver))
        test_results.append(test_complete_search_flow(driver))

        # Calculate results
        passed = sum(test_results)
        total = len(test_results)
        failed = total - passed

        # Display summary
        print("\n" + "="*50)
        print(f"    TEST RESULTS: {passed}/{total} PASSED")
        if failed > 0:
            print(f"    {failed} test(s) failed")
        print("="*50)

    except Exception as e:
        print(f"\n✗ Test suite error: {str(e)}")

    finally:
        # Cleanup
        if driver:
            driver.quit()
            print("\nBrowser closed.")
