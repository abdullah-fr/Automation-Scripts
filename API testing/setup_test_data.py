import requests

def setup_test_student():
    """Create a test student with specific data"""

    # Create student with empty name to match the test expectation
    requestbody = {
        "name": "",
        "Courses": ["API", "Rest"]
    }

    response = requests.post(
        url="http://localhost:3000/studentdata",
        headers={"Content-Type": "application/json"},
        json=requestbody
    )

    print(f"Created student: {response.json()}")
    print(f"Status: {response.status_code}")

    return response.json()

if __name__ == "__main__":
    student = setup_test_student()
    print(f"\nUse this URL for testing: http://localhost:3000/studentdata/{student['id']}")
