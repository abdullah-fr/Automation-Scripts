from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

driver = webdriver.Chrome(options=options)

driver.maximize_window()

# search
driver.get("https://search.brave.com/")

driver.find_element(By.ID, "searchbox").send_keys("upwork login")

driver.find_element(By.ID, "submit-llm-button").click()

input()
cuX4m5zG