from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://github.com")

driver.maximize_window()

print(f"Page title: {driver.title}")
print(f"Current URL: {driver.current_url}")
print("✓ Chrome script executed successfully!")

driver.quit()