test_cases = [
    {"id": "TC-01", "module": "Pricing", "priority": "High",  "input": "AI helps in pricing", "expected": "IMPORTANT", "run": True},
    {"id": "TC-02", "module": "Login", "priority": "Low", "input": "", "expected": "FAIL", "run": False},
    {"id": "TC-03", "module": "Logout", "priority": "Medium", "input": "System ERROR occurred", "expected": "FAIL", "run": False},
    {"id": "TC-04", "module": "Pricing", "priority": "High", "input": "Ok", "expected": "WARNING", "run": True},
    {"id": "TC-05", "module": "Login", "priority": "Low", "input": "AI improves sales efficiency", "expected": "PASS", "run": True}
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

passed_count = 0
failed_count = 0
skipped_count = 0

for tc in test_cases:
    if not tc["run"]:
        print (f'{tc["id"]} | Skipped')
        skipped_count += 1
        continue

    actual_result = evaluate_response(tc["input"])
    expected_result = tc["expected"]

    if actual_result == expected_result:
        status = "PASS"
        #print(f'{tc["id"]} | Module: {tc["module"]} | Priority: {tc["priority"]} | Expected: {expected_result} | Actual: {actual_result} → PASS')
        passed_count += 1
    else:
        status = "FAIL"
        #print(f'{tc["id"]} | Module: {tc["module"]} | Priority: {tc["priority"]} | Expected: {expected_result} | Actual: {actual_result} → FAIL')
        failed_count += 1
    
    print(f'{tc["id"]} | Module: {tc["module"]} | Priority: {tc["priority"]} | Expected: {expected_result} | Actual: {actual_result} → {status}')

print(f"Total Passed: {passed_count}")
print(f"Total Failed: {failed_count}")
print(f"Total Skipped: {skipped_count}")