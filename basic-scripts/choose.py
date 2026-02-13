from selenium import webdriver

print("Choose a browser:")
print("1. Brave")
print("2. Chrome")
print("3. Firefox")

choice = input("\nEnter your choice (1-3): ")

try:
    if choice == "1":
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        driver = webdriver.Chrome(options=options)
        print("Opening Brave...")
    elif choice == "2":
        driver = webdriver.Chrome()
        print("Opening Chrome...")
    elif choice == "3":
        driver = webdriver.Firefox()
        print("Opening Firefox...")
    else:
        print("Invalid choice!")
        exit()

    driver.get("https://github.com")
    driver.maximize_window()

    input("\nPress Enter to close the browser...")

except Exception as e:
    print(f"\nError: {e}")
    print("Make sure the browser is installed and configured properly.")
