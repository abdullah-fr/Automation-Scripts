from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys

# Use headless mode only in CI environment
chrome_options = Options()
if os.getenv('CI'):  # GitHub Actions sets CI=true
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Test Case 1: Navigate to GitHub
    print("Test 1: Navigating to GitHub...")
    driver.get("https://github.com")
    driver.maximize_window()
    assert "GitHub" in driver.title, "GitHub title not found"
    print(f"✓ Page title: {driver.title}")

    # Test Case 2: Verify URL (intentionally failing)
    print("\nTest 2: Verifying URL...")
    current_url = driver.current_url
    assert "google.com" in current_url, "Expected google.com but got different domain"
    print(f"✓ Current URL: {current_url}")

    # Test Case 3: Check page loaded (search for specific element)
    print("\nTest 3: Checking page elements...")
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Wait for page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    print("✓ Page body loaded successfully")

    # Test Case 4: Verify page is interactive
    print("\nTest 4: Verifying page interactivity...")
    page_source = driver.page_source
    assert len(page_source) > 0, "Page source is empty"
    print(f"✓ Page source length: {len(page_source)} characters")

    print("\n" + "="*50)
    print("✓ All test cases passed successfully!")
    print("="*50)

except AssertionError as e:
    print(f"\n✗ Test failed: {e}")
    sys.exit(1)
except Exception as e:
    print(f"\n✗ Error occurred: {e}")
    sys.exit(1)
finally:
    if not os.getenv('CI'):
        input("\nPress Enter to close the browser...")
    driver.quit()