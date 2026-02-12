from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://github.com")

driver.maximize_window()

input()