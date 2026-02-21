"""
Master Test Runner
Runs smoke tests first, then regression tests if smoke passes
All tests are now in test_demo_app.py with pytest markers
"""

import subprocess
import sys


def run_smoke_tests():
    """Run smoke tests first"""
    print("\n" + "="*70)
    print("🔥 STEP 1: RUNNING SMOKE TESTS")
    print("="*70)
    print("Quick sanity checks to verify critical functionality...")
    print("="*70 + "\n")

    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "test_demo_app.py",
        "-v",
        "-m", "smoke",
        "--html=demo_app_test_report.html",
        "--self-contained-html"
    ])

    return result.returncode


def run_regression_tests():
    """Run regression tests with parallel execution"""
    print("\n" + "="*70)
    print("🔄 STEP 2: RUNNING REGRESSION TESTS (PARALLEL EXECUTION)")
    print("="*70)
    print("Comprehensive tests running on 4 parallel workers...")
    print("="*70 + "\n")

    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "test_demo_app.py",
        "-v",
        "-m", "regression",
        "-n", "4",  # 4 parallel workers
        "--html=demo_app_test_report.html",
        "--self-contained-html"
    ])

    return result.returncode


def run_all_tests():
    """Run all tests (smoke + regression) in one go"""
    print("\n" + "="*70)
    print("🚀 RUNNING ALL TESTS (SMOKE + REGRESSION)")
    print("="*70)
    print("Running 20 tests with parallel execution...")
    print("="*70 + "\n")

    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "test_demo_app.py",
        "-v",
        "-n", "4",  # 4 parallel workers
        "--html=demo_app_test_report.html",
        "--self-contained-html"
    ])

    return result.returncode


def main():
    """Main test execution flow"""
    import sys

    # Check if user wants to run all tests at once
    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        result = run_all_tests()
        print("\n" + "="*70)
        print("📊 FINAL RESULTS")
        print("="*70)
        if result == 0:
            print("✅ ALL TESTS PASSED! (5 Smoke + 15 Regression)")
        else:
            print("❌ SOME TESTS FAILED")
        print("="*70)
        print("\n📄 Test Report: demo_app_test_report.html")
        print("="*70 + "\n")
        sys.exit(result)

    # Default: Run smoke first, then regression
    print("\n" + "="*70)
    print("🚀 AUTOMATED TEST SUITE EXECUTION")
    print("="*70)
    print("Strategy: Smoke → Regression (if smoke passes)")
    print("="*70)

    # Run smoke tests
    smoke_result = run_smoke_tests()

    if smoke_result != 0:
        print("\n" + "="*70)
        print("❌ SMOKE TESTS FAILED!")
        print("="*70)
        print("Skipping regression tests due to smoke test failures.")
        print("Fix critical issues first before running full regression.")
        print("="*70 + "\n")
        sys.exit(1)

    print("\n" + "="*70)
    print("✅ SMOKE TESTS PASSED!")
    print("="*70)
    print("Proceeding with regression testing...")
    print("="*70)

    # Run regression tests
    regression_result = run_regression_tests()

    print("\n" + "="*70)
    print("📊 FINAL RESULTS")
    print("="*70)

    if regression_result == 0:
        print("✅ Smoke Tests: PASSED (5 tests)")
        print("✅ Regression Tests: PASSED (15 tests)")
        print("\n🎉 ALL TESTS PASSED! Application is stable.")
    else:
        print("✅ Smoke Tests: PASSED (5 tests)")
        print("❌ Regression Tests: FAILED")
        print("\n⚠️  Some regression tests failed. Check report for details.")

    print("="*70)
    print("\n📄 Test Report: demo_app_test_report.html")
    print("="*70 + "\n")

    sys.exit(regression_result)


if __name__ == "__main__":
    main()
