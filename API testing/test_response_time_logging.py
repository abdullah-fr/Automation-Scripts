import requests
import time
import pytest

def test_response_time_and_logging():
    """Test response time and logging - Python equivalent of Java REST Assured"""

    url = "http://localhost:3000/studentdata/1"

    # Make GET request and measure time
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    # Calculate response time in milliseconds
    response_time_ms = (end_time - start_time) * 1000

    # Print response time
    print(f"Response time: {response_time_ms:.0f}ms")

    # Assert response time is less than 2000ms (2 seconds)
    assert response_time_ms < 2000, "API response is too slow"

    # Get response body as string
    response_body = response.text

    # Print response body
    print(f"Response Body: {response_body}")

    print(f"\n✓ Test passed!")
    print(f"Status Code: {response.status_code}")
    print(f"Response Time: {response_time_ms:.2f}ms")
    print(f"Response Body: {response_body}")

if __name__ == "__main__":
    test_response_time_and_logging()
