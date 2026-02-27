import requests
import pytest

def parse_json():
    """Parse JSON response and extract specific field - Python equivalent of Java REST Assured"""

    url = "http://localhost:3000/studentdata/1"

    # Make GET request and extract "Courses" field
    response = requests.get(url)
    courses = response.json().get("Courses")

    # Print the courses
    print(courses)

    # Assert courses is not null
    assert courses is not None, "Courses should not be null"

    print(f"✓ Test passed!")
    print(f"Courses: {courses}")
    print(f"Full Response: {response.json()}")

if __name__ == "__main__":
    parse_json()
