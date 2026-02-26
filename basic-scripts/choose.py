from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys

# In CI, automatically choose Chrome
if os.getenv('CI'):
    choice = "2"
    print("CI Environment detected - using Chrome")
else:
    print("Choose a browser:")
    print("1. Brave")
    print("2. Chrome")
    print("3. Firefox")
    choice = input("\nEnter your choice (1-3): ")

try:
    if choice == "1":
        options = Options()
        options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        driver = webdriver.Chrome(options=options)
        print("Opening Brave...")
    elif choice == "2":
        options = Options()
        if os.getenv('CI'):
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        print("Opening Chrome...")
    elif choice == "3":
        driver = webdriver.Firefox()
        print("Opening Firefox...")
    else:
        print("Invalid choice!")
        sys.exit(1)

    driver.get("https://github.com")
    driver.maximize_window()

    print(f"✓ Browser opened successfully")
    print(f"✓ Page title: {driver.title}")

    if not os.getenv('CI'):
        input("\nPress Enter to close the browser...")

    driver.quit()

except Exception as e:
    print(f"\n✗ Error: {e}")
    print("Make sure the browser is installed and configured properly.")
    sys.exit(1)
