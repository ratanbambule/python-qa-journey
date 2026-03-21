test_cases = [
    {"id": "TC-01", "output": "AI helps in sales"},
    {"id": "TC-03", "output": ""},
    {"id": "TC-04", "output": "404 ERROR"},
    {"id": "TC-05", "output": "Ok"},
    {"id": "TC-02", "output": "AI helps in pricing"},
]

for test_case in test_cases:
    response = test_case["output"]

    print("Running test case:", test_case["id"])

    if response.strip() == "":
        print("FAIL -", test_case["id"])
    elif "error" in response.strip().lower():
        print("FAIL -", test_case["id"])
    elif "pricing" in response.strip().lower():
        print("Important -", test_case["id"])
    elif len(response) < 10:
        print("WARNING -", test_case["id"])
    else:
        print("PASS -", test_case["id"])


print("--------------------------------")
print("--------------------------------")
print("--------------------------------")

print("Improved version of above code")


for test_case in test_cases:
    response = test_case["output"]
    clean_response = response.strip().lower()

    if clean_response == "":
        result = "FAIL"

    elif "error" in clean_response:
        result = "FAIL"

    elif "pricing" in clean_response:
        result = "IMPORTANT"

    elif len(clean_response) < 10:
        result = "WARNING"

    else:
        result = "PASS"

    print(f"{test_case['id']} → {result}")