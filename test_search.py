# IMPORTS SECTION
# logging: Built-in Python module to write logs to a file for debugging and tracking
import logging

# selenium webdriver: Main library to control the browser automatically
from selenium import webdriver

# By: Used to locate elements on webpage (by ID, class, xpath, etc.)
from selenium.webdriver.common.by import By

# WebDriverWait: Makes selenium wait for elements to appear before interacting
from selenium.webdriver.support.ui import WebDriverWait

# expected_conditions (EC): Conditions to wait for (element present, clickable, etc.)
from selenium.webdriver.support import expected_conditions as EC

# Exceptions: Special error types that selenium can throw
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# LOGGING CONFIGURATION
# This sets up how we save test execution details to logs.txt
logging.basicConfig(
    filename='logs.txt',              # Save logs to this file
    level=logging.INFO,                # Log level: INFO, WARNING, ERROR
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format: timestamp - level - message
    filemode='a'                       # 'a' = append mode (keeps history of all runs)
)

# Create a logger object to write messages to the log file
logger = logging.getLogger(__name__)


# FUNCTION: Setup Browser Driver
# This function initializes and configures the Brave browser for testing
def setup_driver():
    logger.info("Setting up Brave browser")  # Log the start of browser setup

    # Create Chrome options object (Brave uses Chromium engine)
    options = webdriver.ChromeOptions()
    # Tell selenium where Brave browser is installed on this Mac
    options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

    # Create the browser driver instance with our options
    driver = webdriver.Chrome(options=options)

    # Maximize the browser window for better visibility during testing
    driver.maximize_window()

    logger.info("Browser launched and maximized successfully")  # Log success
    return driver  # Return the driver object so other functions can use it


# TEST 1: Navigate to Brave Search
# Purpose: Verify that the browser can successfully load the Brave Search homepage
def test_navigate_to_brave_search(driver):
    logger.info("Test 1: Navigate to Brave Search")  # Log test start
    try:
        # Navigate to Brave Search URL
        driver.get("https://search.brave.com/")

        # Log which URL we actually ended up at
        logger.info(f"Navigated to URL: {driver.current_url}")

        # ASSERTION: Check if "brave.com" is in the current URL
        # If not, this will raise an AssertionError and test fails
        assert "brave.com" in driver.current_url

        # If we reach here, test passed
        logger.info("✓ Test 1 PASSED: Navigation successful")
        print("✓ Test 1 PASSED: Navigate to Brave Search")
        return True  # Return True = test passed

    except Exception as e:
        # If any error occurs (network issue, assertion fail, etc.), catch it here
        logger.error(f"✗ Test 1 FAILED: Navigation failed - {str(e)}")
        print(f"✗ Test 1 FAILED: {str(e)}")
        return False  # Return False = test failed


# TEST 2: Verify Search Box Exists
# Purpose: Check if the search input box is present on the page
def test_search_box_exists(driver):
    logger.info("Test 2: Validate search box exists")  # Log test start
    try:
        # Navigate to Brave Search
        driver.get("https://search.brave.com/")

        # Create a wait object: wait up to 10 seconds for elements to appear
        wait = WebDriverWait(driver, 10)

        # Wait until search box with ID="searchbox" is present in the page DOM
        # EC.presence_of_element_located checks if element exists (not necessarily visible)
        search_box = wait.until(EC.presence_of_element_located((By.ID, "searchbox")))

        # ASSERTION: Verify the search_box object is not None
        assert search_box is not None

        # Test passed
        logger.info("✓ Test 2 PASSED: Search box found")
        print("✓ Test 2 PASSED: Search box exists")
        return True

    except TimeoutException:
        # Specific error: Element not found within 10 seconds
        logger.error("✗ Test 2 FAILED: Search box not found within timeout")
        print("✗ Test 2 FAILED: Search box not found")
        return False

    except Exception as e:
        # Any other error
        logger.error(f"✗ Test 2 FAILED: Error finding search box - {str(e)}")
        print(f"✗ Test 2 FAILED: {str(e)}")
        return False


# TEST 3: Verify Search Box Is Interactable
# Purpose: Check if we can type text into the search box
def test_search_box_is_interactable(driver):
    logger.info("Test 3: Validate search box is interactable")  # Log test start
    try:
        # Navigate to Brave Search
        driver.get("https://search.brave.com/")

        # Create wait object
        wait = WebDriverWait(driver, 10)

        # Wait until search box is clickable (visible, enabled, and ready for interaction)
        # EC.element_to_be_clickable checks if element is both visible AND enabled
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchbox")))

        # Type "upwork login" into the search box
        search_box.send_keys("upwork login")
        logger.info("✓ Successfully entered text in search box")

        # Get the actual value from the search box to verify text was entered
        entered_text = search_box.get_attribute("value")

        # ASSERTION: Verify that our text is in the search box
        assert "upwork login" in entered_text

        # Test passed
        logger.info(f"✓ Test 3 PASSED: Verified text entered - {entered_text}")
        print("✓ Test 3 PASSED: Search box is interactable")
        return True

    except Exception as e:
        # Any error during interaction
        logger.error(f"✗ Test 3 FAILED: Search box interaction failed - {str(e)}")
        print(f"✗ Test 3 FAILED: {str(e)}")
        return False


# TEST 4: Verify Search Button Exists
# Purpose: Check if the search submit button is present on the page
def test_search_button_exists(driver):
    logger.info("Test 4: Validate search button exists")  # Log test start
    try:
        # Navigate to Brave Search
        driver.get("https://search.brave.com/")

        # Create wait object
        wait = WebDriverWait(driver, 10)

        # Wait until search button with ID="submit-llm-button" is present
        search_button = wait.until(EC.presence_of_element_located((By.ID, "submit-llm-button")))

        # ASSERTION: Verify button object is not None
        assert search_button is not None

        # Test passed
        logger.info("✓ Test 4 PASSED: Search button found")
        print("✓ Test 4 PASSED: Search button exists")
        return True

    except TimeoutException:
        # Button not found within 10 seconds
        logger.error("✗ Test 4 FAILED: Search button not found within timeout")
        print("✗ Test 4 FAILED: Search button not found")
        return False

    except Exception as e:
        # Any other error
        logger.error(f"✗ Test 4 FAILED: Error finding search button - {str(e)}")
        print(f"✗ Test 4 FAILED: {str(e)}")
        return False


# TEST 5: Complete End-to-End Search Flow
# Purpose: Test the entire search process from start to finish
def test_complete_search_flow(driver):
    logger.info("Test 5: Complete search flow execution")  # Log test start
    try:
        # STEP 1: Navigate to Brave Search homepage
        driver.get("https://search.brave.com/")
        logger.info("Step 1: Navigated to Brave Search")

        # STEP 2: Wait for and locate the search box
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchbox")))
        logger.info("Step 2: Search box located")

        # STEP 3: Type search query into the search box
        search_box.send_keys("upwork login")
        logger.info("Step 3: Entered search query 'upwork login'")

        # STEP 4: Wait for and locate the search button
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-llm-button")))
        logger.info("Step 4: Search button located")

        # STEP 5: Click the search button to submit the search
        search_button.click()
        logger.info("Step 5: Clicked search button")

        # STEP 6: Wait for URL to change (indicates search results loaded)
        # lambda d: checks if current URL is different from homepage
        wait.until(lambda d: d.current_url != "https://search.brave.com/")
        logger.info(f"Step 6: URL changed to: {driver.current_url}")

        # ASSERTION: Verify that we're no longer on the homepage
        # (we should be on search results page)
        assert driver.current_url != "https://search.brave.com/"

        # Test passed - entire search flow completed successfully
        logger.info("✓ Test 5 PASSED: Complete search flow executed successfully")
        print("✓ Test 5 PASSED: Complete search flow")
        return True

    except Exception as e:
        # Any error during the search flow
        logger.error(f"✗ Test 5 FAILED: Complete search flow failed - {str(e)}")
        print(f"✗ Test 5 FAILED: {str(e)}")
        return False


# FUNCTION: Get execution number from log file
# Counts how many times tests have been run by reading the log file
def get_execution_number():
    try:
        with open('logs.txt', 'r') as f:
            content = f.read()
            # Count how many "TEST EXECUTION" headers exist
            count = content.count('TEST EXECUTION #')
            return count + 1  # Return next execution number
    except FileNotFoundError:
        # If logs.txt doesn't exist yet, this is execution #1
        return 1


# MAIN EXECUTION BLOCK
# This code only runs when you execute this file directly (not when imported)
if __name__ == "__main__":
    # Get the execution number for this run
    execution_num = get_execution_number()

    # Log execution header with number
    logger.info("\n\n\n\n\n" + "="*60)
    logger.info(f"TEST EXECUTION #{execution_num}")
    logger.info("=" * 60)
    logger.info("=== Starting Brave Search Test Suite ===")

    # Print test suite header
    print("\n" + "="*50)
    print(f"    TEST EXECUTION #{execution_num}")
    print("    BRAVE SEARCH AUTOMATION TEST SUITE")
    print("="*50 + "\n")

    # Initialize variables
    driver = None              # Will hold the browser driver instance
    test_results = []          # Will store True/False results from each test

    try:
        # SETUP: Launch the browser
        driver = setup_driver()

        # RUN ALL TESTS: Each test returns True (passed) or False (failed)
        # We append each result to test_results list
        test_results.append(test_navigate_to_brave_search(driver))      # Test 1
        test_results.append(test_search_box_exists(driver))             # Test 2
        test_results.append(test_search_box_is_interactable(driver))    # Test 3
        test_results.append(test_search_button_exists(driver))          # Test 4
        test_results.append(test_complete_search_flow(driver))          # Test 5

        # CALCULATE RESULTS
        # sum(test_results) counts how many True values (passed tests)
        passed = sum(test_results)
        total = len(test_results)    # Total number of tests
        failed = total - passed      # Calculate failed tests

        # DISPLAY RESULTS SUMMARY
        print("\n" + "="*50)
        print(f"    TEST RESULTS: {passed}/{total} PASSED")
        if failed > 0:
            print(f"    {failed} test(s) failed")
        print("="*50)

        # Log final results
        logger.info(f"=== Test Suite Complete: {passed}/{total} tests passed ===")

        # Print final message based on results
        if passed == total:
            print("\n✓ All tests passed! Check logs.txt for details.")
        else:
            print(f"\n✗ {failed} test(s) failed. Check logs.txt for details.")

    except Exception as e:
        # If any unexpected error occurs during test execution
        logger.error(f"✗ Test suite error: {str(e)}")
        print(f"\n✗ Test suite error: {str(e)}")

    finally:
        # CLEANUP: This always runs, even if there were errors
        # Close the browser to free up resources
        if driver:
            logger.info("Closing browser")
            driver.quit()  # Close browser and end WebDriver session
            logger.info("Browser closed successfully")
            print("\nBrowser closed.")
