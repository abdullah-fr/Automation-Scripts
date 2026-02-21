# How to Run Demo App Tests

## Step 1: Start the Demo App

Open Terminal 1:
```bash
python3 demo_app.py
```

Keep this running! You should see:
```
Demo app running at http://localhost:5000
Test credentials: test@example.com / Test123!
```

## Step 2: Run the Tests

Open Terminal 2 (or new terminal tab):
```bash
python3 test_demo_app.py
```

## Step 3: View the HTML Report

After tests complete, open the report:
```bash
open demo_app_test_report.html
```

Or just double-click `demo_app_test_report.html` in Finder.

## What You'll See

**HTML Report includes:**
- ✅ Test summary (passed/failed)
- ⏱️ Execution time for each test
- 📊 Overall statistics
- 🖥️ Environment info (Python version, OS, etc.)
- 📝 Detailed test results
- ❌ Error details (if any tests fail)

## Test Coverage

**14 Tests Total:**
- 6 Login tests
- 6 Signup tests
- 2 Navigation tests

All tests should pass! 🎉

## Tips

- Make sure demo app is running before tests
- Tests take about 30-40 seconds
- Browser will open and close automatically
- HTML report is self-contained (no internet needed)
- You can share the HTML report file with anyone
