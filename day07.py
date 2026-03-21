test_cases = [
    {"id": "TC-01", "input": "AI helps in pricing", "expected": "IMPORTANT"},
    {"id": "TC-02", "input": "", "expected": "FAIL"},
    {"id": "TC-03", "input": "System ERROR occurred", "expected": "FAIL"},
    {"id": "TC-04", "input": "Ok", "expected": "WARNING"},
    {"id": "TC-05", "input": "AI improves sales efficiency", "expected": "PASS"}
]

def evaluate_response(response):
    clean_response = response.strip().lower()

    if clean_response == "":
        return "FAIL"
    elif "error" in clean_response:
        return "FAIL"
    elif "pricing" in clean_response:
        return "IMPORTANT"
    elif len(clean_response) < 10:
        return "WARNING"
    else:
        return "PASS" 

pass_count = 0
fail_count = 0

for test_case in test_cases:
    actual_result = evaluate_response(test_case["input"])
    expected_result = test_case["expected"]


    if actual_result == expected_result :
        print(f'{test_case["id"]} → Expected: {test_case["expected"]} | Actual: {actual_result} → PASS')
        pass_count += 1
    else:
        print(f'{test_case["id"]} → Expected: {test_case["expected"]} | Actual: {actual_result} → FAIL')
        fail_count += 1

print (f"Total Passed: {pass_count}")
print (f"Total Failed: {fail_count}")