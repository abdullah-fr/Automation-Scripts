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
├── API testing/               # API test automation
│   ├── mock_server.py        # Flask mock API server
│   ├── simple_post_test.py   # Simple POST request test
│   ├── test_get_post.py      # GET request with assertions
│   └── setup_test_data.py    # Test data setup utility
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
A complete login/signup application with comprehensive test suite including smoke, regression, and data-driven testing:

```bash
# Terminal 1: Start the demo app
cd functional-testing
python3 demo_app.py

# Terminal 2: Run all tests (smoke + regression + data-driven in parallel)
cd functional-testing
python3 test_demo_app.py

# Or use the master runner:
python3 run_all_tests.py          # Runs smoke first, then regression
python3 run_all_tests.py --all    # Runs all tests at once

# Run specific test types:
pytest test_demo_app.py -m smoke       # Only smoke tests (5 tests)
pytest test_demo_app.py -m regression  # Only regression tests (52+ tests)
pytest test_demo_app.py -m datadriven  # Only data-driven tests (37 tests)
pytest test_demo_app.py -m login       # Only login tests
pytest test_demo_app.py -m signup      # Only signup tests
pytest test_demo_app.py -m validation  # Only validation tests
```

**Features:**
- Flask-based web application
- 57+ comprehensive tests in one file (test_demo_app.py)
- Smoke Testing: 5 critical path tests
- Regression Testing: 15 comprehensive tests
- Data-Driven Testing: 37+ parametrized tests with large datasets
- Single unified HTML report (demo_app_test_report.html)
- Professional test structure with explicit waits and pytest markers
- Parallel execution with pytest-xdist (4 workers)

**Test Organization:**

1. **Smoke Tests** (@pytest.mark.smoke): Quick sanity checks (5 tests)
   - App is running
   - Login/Signup pages load
   - Valid login works
   - Navigation works

2. **Regression Tests** (@pytest.mark.regression): Comprehensive coverage (15 tests)
   - 6 Login tests (@pytest.mark.login)
   - 6 Signup tests (@pytest.mark.signup)
   - 3 Navigation tests (@pytest.mark.navigation)
   - Validation tests (@pytest.mark.validation)

3. **Data-Driven Tests** (@pytest.mark.datadriven): Large dataset testing (37+ tests)
   - 10 invalid login scenarios (empty fields, wrong passwords, invalid emails)
   - 11 invalid signup scenarios (empty fields, mismatched passwords, existing emails)
   - 5 valid signup scenarios (multiple user registrations)
   - 5 password length validation tests (1-5 character passwords)
   - 6 email format validation tests (various invalid email formats)
   - Uses @pytest.mark.parametrize for data-driven approach

**Test Data Sets:**
- INVALID_LOGIN_DATA: 10 test cases
- INVALID_SIGNUP_DATA: 11 test cases
- VALID_SIGNUP_DATA: 5 test cases
- PASSWORD_VALIDATION_DATA: 5 test cases
- EMAIL_FORMAT_DATA: 6 test cases

**Execution:**
- All tests run in headless mode for speed
- Parallel execution with 4 workers (pytest-xdist)
- Single unified HTML report with all results

**Why this approach?**
Testing systems you control provides reliable, reproducible results. Data-driven testing allows you to test multiple scenarios with minimal code duplication. This is how professional QA engineers work - using parametrized tests to cover edge cases efficiently.

## 🔌 API Testing

Comprehensive API testing framework with Python and requests library:

```bash
# Terminal 1: Start the mock API server
cd "API testing"
python3 mock_server.py

# Terminal 2: Run tests
python3 simple_post_test.py    # Simple POST request
python3 test_get_post.py       # GET with assertions
python3 setup_test_data.py     # Setup test data
```

**Features:**
- Mock Flask API server for testing
- POST request automation (create student data)
- GET request with assertions (validate responses)
- Response validation (status codes, JSON data)
- Python equivalent of Java REST Assured tests

**Test Scripts:**
1. **mock_server.py**: Flask-based mock API server
   - POST /studentdata - Create student
   - GET /studentdata - Get all students
   - GET /studentdata/:id - Get single student

2. **simple_post_test.py**: Basic POST request test
   - Creates student with name and courses
   - Validates status code 201
   - Prints formatted JSON response

3. **test_get_post.py**: GET request with assertions
   - Retrieves student data
   - Asserts status code 200
   - Validates response fields
   - Python equivalent of Java REST Assured test

4. **setup_test_data.py**: Test data utility
   - Creates test students
   - Returns student IDs for testing

**Why API Testing?**
API testing validates backend functionality independently of UI, enabling faster test execution and easier continuous integration. This approach mirrors real-world API testing workflows used in professional QA environments.
