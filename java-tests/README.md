# Java TestNG Test Suite

This folder contains Java-based Selenium tests using TestNG framework for Brave Search automation.

## Project Structure

```
java-tests/
├── pom.xml                          # Maven configuration
├── testng.xml                       # TestNG suite configuration
├── src/
│   └── test/
│       └── java/
│           └── BraveSearchTest.java # Test class
└── README.md
```

## Setup

### Prerequisites
- Java 11 or higher
- Maven 3.6+
- Brave Browser installed

### Install Maven (macOS)
```bash
brew install maven
```

### Verify Installation
```bash
java -version
mvn -version
```

## Running Tests

### Using Maven
```bash
# Run all tests
mvn test

# Run with verbose output
mvn test -Dtestng.verbose=2

# Clean and run tests
mvn clean test
```

### Using TestNG XML
```bash
mvn test -DsuiteXmlFile=testng.xml
```

### Run Specific Test
```bash
mvn test -Dtest=BraveSearchTest#testNavigateToBraveSearch
```

## Dependencies

Managed automatically by Maven (defined in `pom.xml`):
- Selenium Java 4.16.1
- TestNG 7.8.0

## Test Reports

After running tests, reports are generated in:
- `target/surefire-reports/` - Maven test reports
- `test-output/` - TestNG HTML reports
