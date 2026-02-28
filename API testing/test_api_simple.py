import requests
import time

# ----------------------------
# ⚙️ Configuration
# ----------------------------
API_ENDPOINT = "https://jsonplaceholder.typicode.com/users/1"
REQUIRED_KEYS = ["id", "name", "username", "email"]
RESPONSE_TIME_THRESHOLD = 2000  # milliseconds

# ----------------------------
# 🧪 API Test Function
# ----------------------------
def test_api():
    print("\n=== API Test Report ===\n")

    try:
        # Make API request and measure time
        start_time = time.time()
        response = requests.get(API_ENDPOINT)
        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)

        # Parse response
        body = response.json()
        headers = dict(response.headers)

        # Test results
        print(f"API Endpoint: {API_ENDPOINT}")
        print(f"Status Code: {response.status_code}")
        print(f"Pass_Status_Code: {response.status_code < 400}")
        print()

        print(f"Response Time (ms): {response_time}")
        print(f"Pass_Response_Time: {response_time < RESPONSE_TIME_THRESHOLD}")
        print()

        print(f"Response Body: {body}")
        print(f"Pass_Response_Body: {isinstance(body, dict) and len(body) > 0}")
        print()

        print(f"Headers: {headers}")
        print(f"Pass_Headers: {len(headers) > 0}")
        print()

        # Schema validation
        schema_pass = all(key in body for key in REQUIRED_KEYS)
        print(f"Schema Validation (Required Keys: {REQUIRED_KEYS}): {schema_pass}")
        print()

        # Data validation
        data_valid = "username" in body and len(body.get("username", "")) > 0
        print(f"Data Validation (username exists and not empty): {data_valid}")
        print()

        # Overall result
        all_passed = (
            response.status_code < 400 and
            response_time < RESPONSE_TIME_THRESHOLD and
            schema_pass and
            data_valid
        )
        print(f"Overall Test Result: {'✅ PASSED' if all_passed else '❌ FAILED'}")

    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")

# ----------------------------
# Run Test
# ----------------------------
if __name__ == "__main__":
    test_api()