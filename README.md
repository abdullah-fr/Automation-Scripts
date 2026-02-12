# Automation-Scripts

A collection of Python Selenium automation scripts for browser testing and web automation tasks.

## 📋 Overview

This repository contains various Selenium WebDriver scripts for automating browser interactions, with a focus on testing and browser automation across different browsers (Brave, Chrome, Firefox).

## 🚀 Features

- Multi-browser support (Brave, Chrome, Firefox)
- Interactive browser selection
- Automated search functionality
- Comprehensive test suite with logging
- Detailed execution logs for debugging

## 📁 Project Structure

```
Automation-Scripts/
├── brave.py           # Launch Brave browser and navigate to GitHub
├── chrome.py          # Launch Chrome browser and navigate to GitHub
├── choose.py          # Interactive browser selector
├── search.py          # Automated search on Brave Search
├── test_search.py     # Complete test suite with 5 automated tests
├── logs.txt           # Test execution logs
└── README.md          # Project documentation
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/abdullah-fr/Automation-Scripts.git
cd Automation-Scripts
```

2. Install required dependencies:
```bash
pip install selenium
```

3. Install browser drivers:
   - Chrome/Brave: Download [ChromeDriver](https://chromedriver.chromium.org/)
   - Firefox: Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

## 💻 Usage

### Basic Browser Scripts

**Launch Brave Browser:**
```bash
python brave.py
```

**Launch Chrome Browser:**
```bash
python chrome.py
```

**Interactive Browser Selection:**
```bash
python choose.py
```

### Automated Search

Run automated search on Brave Search:
```bash
python search.py
```

### Test Suite

Run the complete test suite with 5 automated tests:
```bash
python test_search.py
```

The test suite includes:
1. Navigate to Brave Search
2. Verify search box exists
3. Verify search box is interactable
4. Verify search button exists
5. Complete end-to-end search flow

## 📊 Test Results

Test execution results are automatically logged to `logs.txt` with:
- Timestamp for each test
- Pass/fail status
- Detailed error messages
- Execution number tracking

## ⚙️ Configuration

For macOS users, the Brave browser path is set to:
```python
"/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
```

Update this path in the scripts if your browser is installed in a different location.

## 📝 Requirements

- Python 3.x
- Selenium WebDriver
- Chrome/Brave/Firefox browser
- Corresponding browser driver (ChromeDriver/GeckoDriver)

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

Abdullah - [GitHub Profile](https://github.com/abdullah-fr)
