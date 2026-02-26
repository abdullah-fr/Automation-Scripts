from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Use headless mode only in CI environment
chrome_options = Options()

if os.getenv('CI'):  # GitHub Actions sets CI=true
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
else:
    chrome_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.maximize_window()

    # Search
    driver.get("https://search.brave.com/")
    time.sleep(2)

    driver.find_element(By.ID, "searchbox").send_keys("upwork login")
    time.sleep(1)

    driver.find_element(By.ID, "submit-llm-button").click()
    time.sleep(2)

    print("✓ Search executed successfully")
    print(f"✓ Current URL: {driver.current_url}")

    if not os.getenv('CI'):
        input("\nPress Enter to close the browser...")

except Exception as e:
    print(f"✗ Error: {e}")
    exit(1)
finally:
    driver.quit()
