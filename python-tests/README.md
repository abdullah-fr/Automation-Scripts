# Python Test Suite

This folder contains Python-based Selenium tests for Brave Search automation.

## Files

- `test_search_pytest.py` - Tests using pytest framework (recommended)
- `test_search_manual.py` - Tests without pytest (manual approach)

## Setup

```bash
# Install dependencies
pip install selenium pytest

# Or using requirements.txt
pip install -r requirements.txt
```

## Running Tests

### With Pytest (Recommended)
```bash
# Run all tests
pytest test_search_pytest.py -v

# Run specific test
pytest test_search_pytest.py::test_navigate_to_brave_search -v

# Run with detailed output
pytest test_search_pytest.py -v -s

# Run in parallel (requires pytest-xdist)
pytest test_search_pytest.py -n 4
```

### Manual Execution
```bash
python test_search_manual.py
```

## Requirements

- Python 3.7+
- Selenium WebDriver
- pytest (for pytest version)
- Brave Browser installed at: `/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`
- ChromeDriver (compatible with your Chrome/Brave version)
