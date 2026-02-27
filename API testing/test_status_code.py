import requests
import pytest

def test_status_code():
    """Test status code validation - Python equivalent of Java REST Assured"""

    url = "http://localhost:3000/studentdata/1"

    # Make GET request
    response = requests.get(url)

    # Extract status code
    statuscode = response.status_code

    # Assert status code equals 200
    assert statuscode == 200, f"Expected Status is 200"

    print(f"✓ Test passed!")
    print(f"Status Code: {statuscode}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_status_code()
