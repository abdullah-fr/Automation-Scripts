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
│   ├── logs.txt
│   └── README.md
│
├── python-tests/              # Python test implementations
│   ├── test_search_pytest.py  # Using pytest framework
│   ├── test_search_manual.py  # Manual approach (no framework)
│   ├── requirements.txt       # Python dependencies
│   └── README.md
│
├── java-tests/                # Java test implementations
│   ├── src/test/java/
│   │   └── BraveSearchTest.java
│   ├── pom.xml               # Maven configuration
│   ├── testng.xml            # TestNG suite config
│   └── README.md
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

### Demo Login/Signup App
We've included a proper demo application to practice automation:

```bash
# Install Flask
pip install flask

# Run demo app
python demo_app.py

# Run tests (in another terminal)
python test_demo_app.py
```

See [AUTOMATION_REALITY_CHECK.md](AUTOMATION_REALITY_CHECK.md) for why testing controlled environments is the professional approach.

**Key Lesson:** Test systems you control, not production sites like Facebook. Our demo app provides 15 reliable, reproducible test cases.
