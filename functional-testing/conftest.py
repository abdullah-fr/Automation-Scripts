"""
Pytest configuration and hooks for enhanced HTML reporting
"""
import pytest
from datetime import datetime


def pytest_html_report_title(report):
    """Customize report title"""
    report.title = "Demo App - Comprehensive Test Report"


def pytest_configure(config):
    """Add custom metadata to report"""
    if hasattr(config, '_metadata'):
        config._metadata['Project'] = 'Demo App - Login/Signup Testing'
        config._metadata['Test Suite'] = 'Smoke + Regression + Data-Driven'
        config._metadata['Tester'] = 'Automation Team'
        config._metadata['Environment'] = 'Local Development'
        config._metadata['Test Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add test description to report"""
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__) if item.function.__doc__ else ''
