import requests

# Step 1: Send GET request to API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Step 2: Print response status code
print("Status Code:", response.status_code)

# Step 3: Convert response to JSON
data = response.json()

# Step 4: Validate status code
if response.status_code == 200:
    print("Status Code Test Passed")
else:
    print("Status Code Test Failed")

# Step 5: Validate response data
if "userId" in data:
    print("Key Validation Passed")
else:
    print("Key Validation Failed")