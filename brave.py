from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

driver = webdriver.Chrome(options=options)

driver.get("https://github.com")

driver.maximize_window()

input()
