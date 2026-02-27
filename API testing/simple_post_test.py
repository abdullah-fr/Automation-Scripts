import requests
import json

def simple_post_test():
    """Simple POST request test - Python equivalent of Java REST Assured"""

    # Request body
    requestbody = {
        "name": "Raj Kumar P",
        "Courses": [
            "API",
            "Rest"
        ]
    }

    # Make POST request
    response = requests.post(
        url="http://localhost:3000/studentdata",
        headers={"Content-Type": "application/json"},
        json=requestbody
    )

    # Print results
    print(f"Status Code: {response.status_code}")
    print(f"Body: {response.text}")

    # Additional response details
    print(f"\nResponse Headers: {dict(response.headers)}")
    print(f"Response Time: {response.elapsed.total_seconds():.2f}s")

    # Parse and pretty print JSON response
    try:
        response_json = response.json()
        print(f"\nFormatted Response:\n{json.dumps(response_json, indent=2)}")
    except:
        print("\nResponse is not JSON format")

if __name__ == "__main__":
    simple_post_test()
