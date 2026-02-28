import requests
import pytest
import json

def test_get_post():
    """Test GET request with proper assertions and output validation"""

    url = "http://localhost:3000/studentdata/1"

    # Expected output values
    expected_status_code = 200
    expected_id = 1
    expected_name = "Abdullah"

    # Make GET request
    print("\n" + "="*60)
    print(f"Making GET request to: {url}")
    print("="*60)

    response = requests.get(url)

    # Print raw response details
    print(f"\n📡 Response Status Code: {response.status_code}")
    print(f"📡 Response Headers: {dict(response.headers)}")
    print(f"\n📄 Raw Response Text:")
    print(response.text)
    print(f"\n📋 Formatted JSON Response:")
    print(json.dumps(response.json(), indent=2))
    print("="*60)

    # Verify status code matches expected
    assert response.status_code == expected_status_code, \
        f"Expected status {expected_status_code}, got {response.status_code}"

    # Convert response to JSON
    response_json = response.json()

    # Validate response structure
    assert isinstance(response_json, dict), \
        "Response should be a JSON object"

    # Extract fields
    student_id = response_json.get("id")
    name = response_json.get("name")

    # Validate ID
    assert student_id is not None, "id should not be null"
    assert isinstance(student_id, int), "id should be an integer"
    assert student_id == expected_id, \
        f"Expected id to be {expected_id}, got {student_id}"

    # Validate name
    assert name is not None, "name should not be null"
    assert isinstance(name, str), "name should be a string"
    assert name.strip() != "", "name should not be empty"
    assert name == expected_name, \
        f"Expected name to be '{expected_name}', got '{name}'"

    # Validate complete response structure
    expected_response = {
        "id": expected_id,
        "name": expected_name
    }
    assert response_json == expected_response, \
        f"Response mismatch!\nExpected: {expected_response}\nGot: {response_json}"

    print("\n✅ All validations passed!")
    print(f"   Status Code: {response.status_code} ✓ (Expected: {expected_status_code})")
    print(f"   Student ID: {student_id} ✓ (Expected: {expected_id})")
    print(f"   Name: '{name}' ✓ (Expected: '{expected_name}')")
    print("="*60 + "\n")
