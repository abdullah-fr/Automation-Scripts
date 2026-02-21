# Brave Search Automation Test Suite

Automated testing for Brave Search using Selenium WebDriver with Python (pytest) and Java (TestNG) implementations.

## 📁 Project Structure

```
.
├── basic-scripts/             # Original basic scripts
│   ├── brave.py
│   ├── chrome.py
│   ├── choose.py
│   ├── search.py
│   └── logs.txt
│
├── python-tests/              # Python test implementations
│   ├── test_search_pytest.py  # Using pytest framework
│   ├── test_search_manual.py  # Manual approach (no framework)
│   └── requirements.txt       # Python dependencies
│
├── java-tests/                # Java test implementations
│   ├── src/test/java/
│   │   └── BraveSearchTest.java
│   ├── pom.xml               # Maven configuration
│   └── testng.xml            # TestNG suite config
│
├── functional-testing/        # Demo login/signup app with tests
│   ├── demo_app.py           # Flask web application
│   ├── test_demo_app.py      # Automated tests (14 tests)
│   └── templates/            # HTML templates
│
└── README.md                 # This file
```

## 🧪 Test Coverage

All implementations test the following scenarios:

1. Navigate to Brave Search homepage
2. Verify search box exists
3. Verify search box accepts input
4. Verify search button exists
5. Complete end-to-end search flow

## 🚀 Quick Start

### Python Tests

```bash
# Install dependencies
pip install -r python-tests/requirements.txt

# Run tests with pytest (recommended)
pytest python-tests/test_search_pytest.py -v

# Or run manually without pytest
python python-tests/test_search_manual.py
```

### Java Tests

```bash
# Install Maven (if not already installed)
brew install maven

# Run tests
mvn test -f java-tests/pom.xml
```

## 📊 Framework Comparison

| Feature | Python + pytest | Python Manual | Java + TestNG |
|---------|----------------|---------------|---------------|
| Code Lines | ~70 | ~140 | ~120 |
| Setup/Teardown | Automatic | Manual | Automatic |
| Parallel Execution | ✅ Yes | ❌ No | ✅ Yes |
| Test Reports | ✅ Rich | ⚠️ Basic | ✅ Rich |
| Learning Curve | Easy | Easy | Medium |

## 🔧 Requirements

### Common
- Brave Browser installed at: `/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`
- ChromeDriver (auto-managed by Selenium)
- Internet connection

### Python
- Python 3.7+
- pip package manager

### Java
- Java 11+
- Maven 3.6+

## 🔧 Requirements

## 🎯 Which Framework to Use?

**Use Python + pytest when:**
- You want clean, maintainable code
- You need quick setup and execution
- You prefer Python ecosystem

**Use Java + TestNG when:**
- You're working in Java ecosystem
- You need enterprise-level testing
- Your team is familiar with Java

**Use Python Manual when:**
- You're learning automation basics
- You want to understand fundamentals

## ✅ Verified Working

- ✅ Python pytest tests: All 5 tests passing
- ⏳ Java TestNG tests: Requires Maven installation

## 📝 Notes

- Browser path is configured for macOS (update for Windows/Linux)
- Explicit waits are used (10 seconds timeout)
- Tests run sequentially by default
- For parallel execution: `pytest -n 4` (Python) or configure TestNG (Java)

## 🎓 Learning Resources

### Functional Testing Demo
A complete login/signup application with automated tests including smoke and regression testing:

```bash
# Terminal 1: Start the demo app
cd functional-testing
python3 demo_app.py

# Terminal 2: Run all tests (smoke + regression)
cd functional-testing
python3 run_all_tests.py

# Or run individually:
python3 test_smoke.py        # Quick sanity checks (5 tests)
python3 test_regression.py   # Comprehensive tests (15 tests, parallel)
python3 test_demo_app.py     # Original test suite (14 tests)
```

**Features:**
- Flask-based web application
- Smoke Testing: 5 critical path tests
- Regression Testing: 15 comprehensive tests with parallel execution
- HTML test reports for all suites
- Professional test structure with explicit waits

**Test Strategy:**
1. **Smoke Tests** (test_smoke.py): Quick sanity checks to verify critical functionality
   - App is running
   - Login/Signup pages load
   - Valid login works
   - Navigation works

2. **Regression Tests** (test_regression.py): Comprehensive tests with pytest markers
   - 6 Login tests (@pytest.mark.login)
   - 6 Signup tests (@pytest.mark.signup)
   - 3 Navigation tests (@pytest.mark.navigation)
   - Parallel execution with 4 workers (pytest-xdist)
   - Headless mode for speed

3. **Master Runner** (run_all_tests.py): Runs smoke first, then regression if smoke passes

**Why this approach?**
Testing systems you control provides reliable, reproducible results. This is how professional QA engineers work - not by automating production sites, but by testing controlled environments with proper test strategies.
