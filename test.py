import requests

BASE_URL = "http://localhost:3000"

test_cases = [
    {
        "name": "POST contains all alphabets",
        "method": "post",
        "payload": {"input_string": "The quick brown fox jumps over the lazy dog"},
        "expected_status": 200,
        "expected_response": {"contains_all_alphabets": True},
    },
    {
        "name": "POST missing some alphabets",
        "method": "post",
        "payload": {"input_string": "Hello World"},
        "expected_status": 200,
        "expected_response": {"contains_all_alphabets": False},
    },
    {
        "name": "POST invalid input",
        "method": "post",
        "payload": {"input_string": 12345},
        "expected_status": 400,
        "expected_response": {
            "error": "Invalid input: a valid input_string is required"
        },
    },
    {
        "name": "POST without input",
        "method": "post",
        "expected_status": 400,
        "expected_response": {
            "error": "Invalid input: a valid input_string is required"
        },
    },
    {
        "name": "GET contains all alphabets",
        "method": "get",
        "params": {"input_string": "The quick brown fox jumps over the lazy dog"},
        "expected_status": 200,
        "expected_response": {"contains_all_alphabets": True},
    },
    {
        "name": "GET missing some alphabets",
        "method": "get",
        "params": {"input_string": "Hello World"},
        "expected_status": 200,
        "expected_response": {"contains_all_alphabets": False},
    },
    {
        "name": "GET invalid input",
        "method": "get",
        "params": {"input_string": 12345},
        "expected_status": 200,
        "expected_response": {"contains_all_alphabets": False},
    },
    {
        "name": "GET without input",
        "method": "get",
        "expected_status": 400,
        "expected_response": {
            "error": "Invalid input: a valid input_string is required"
        },
    },
]

for i,test in enumerate(test_cases):
    try:
        print(f"\nTEST {i+1} : {test['name']}")
        if test["method"] == "post":
            response = requests.post(BASE_URL, json=test.get("payload"), timeout=60)
        else:
            response = requests.get(BASE_URL, params=test.get("params"), timeout=60)

        if response.status_code == test["expected_status"]:
            print("expected_status: Passed")
        else:
            print(
                f"expected_status: Failed\n\tExpected status: {test['expected_status']}, got: {response.status_code}"
            )
        if response.json() == test["expected_response"]:
            print("expected_response: Passed")
        else:
            print(
                f"expected_response: Failed\n\tExpected response: {test['expected_response']}, got: {response.json()}"
            )
    except Exception as e:
        print(f"Error: {e}")
