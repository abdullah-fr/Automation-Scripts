import requests
import pytest

def test_field_validations():
    """Test field validations - Python equivalent of Java REST Assured"""

    url = "http://localhost:3000/studentdata/1"

    # Make GET request
    response = requests.get(url)

    # Get response body as JSON
    body = response.json()

    # Validate status code
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    # Validate "name" field is instance of String (str in Python)
    assert isinstance(body.get("name"), str), "name should be a string"

    # Validate "Courses" field is not null
    assert body.get("Courses") is not None, "Courses should not be null"

    # Validate "id" field is greater than 0
    assert body.get("id", 0) > 0, "id should be greater than 0"

    print(f"✓ All validations passed!")
    print(f"Status Code: {response.status_code}")
    print(f"Name: '{body.get('name')}' (type: {type(body.get('name')).__name__})")
    print(f"Courses: {body.get('Courses')}")
    print(f"ID: {body.get('id')}")
    print(f"\nFull Response: {body}")

if __name__ == "__main__":
    test_field_validations()
