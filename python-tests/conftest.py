import pytest
from datetime import datetime

# Custom metadata for the report
def pytest_configure(config):
    config._metadata = {
        'Project': 'Brave Search Automation',
        'Test Suite': 'Python Pytest Tests',
        'Tester': 'Automation Team',
        'Environment': 'macOS',
        'Browser': 'Brave Browser'
    }

def pytest_html_report_title(report):
    report.title = "Brave Search Automation Test Report"
