import requests
import pytest

def test_get_post():
    """Test GET request with assertions - Python equivalent of Java REST Assured"""

    url = "http://localhost:3000/studentdata/1"

    # Make GET request
    response = requests.get(url)

    # Verify status code
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    # Extract name from response
    response_json = response.json()
    name = response_json.get("name")

    # Assertions
    assert name is not None, "name should not be null"
    assert name == "", f"Expected empty string, got '{name}'"

    print(f"✓ Test passed!")
    print(f"Status Code: {response.status_code}")
    print(f"Name: '{name}'")
    print(f"Full Response: {response_json}")

if __name__ == "__main__":
    test_get_post()
