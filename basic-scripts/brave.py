from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Use headless mode only in CI environment
chrome_options = Options()
chrome_options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

if os.getenv('CI'):  # GitHub Actions sets CI=true
    # In CI, use Chrome instead of Brave
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://github.com")
    driver.maximize_window()

    print(f"✓ Brave/Chrome opened successfully")
    print(f"✓ Page title: {driver.title}")
    print(f"✓ Current URL: {driver.current_url}")

    if not os.getenv('CI'):
        input()

except Exception as e:
    print(f"✗ Error: {e}")
    exit(1)
finally:
    driver.quit()
