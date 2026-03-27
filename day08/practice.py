test_cases = [
    {"id": "TC-001", "module" : "inbound agent creation", "priority" : "High", "input" : "Create an agent for pricing", "expected" : "IMPORTANT", "run" : True},
    {"id": "TC-002", "module" : "inbound agent updation", "priority" : "Medium", "input" : " ", "expected" : "FAIL", "run" : True},
    {"id": "TC-003", "module" : "inbound agent deletion", "priority" : "Low", "input" : "Error deleting an agent", "expected" : "FAIL", "run" : True},
    {"id": "TC-004", "module" : "outbound agent creation", "priority" : "High", "input" : "Create an agent for testing", "expected" : "PASS", "run" : True},
    {"id": "TC-005", "module" : "outbound agent updation", "priority" : "Medium", "input" : "Update", "expected" : "WARNING", "run" : False},
]

def evaluate_response(response):
    clean_response = response.strip().lower()

    if clean_response =="":
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
        tc["status"] = "SKIPPED"
        tc["actual"] = None
        tc["notes"] = "Execution skipped based on run flag"
        skipped_count +=1
        continue

    actual_result = evaluate_response(tc["input"])
    tc["actual"] = actual_result

    if actual_result == tc["expected"]:
        tc["status"] = "PASS"
        tc["notes"] = "Matched expected result"
        passed_count +=1
    else:
        tc["status"] = "FAIL"
        tc["notes"] = "Mismatch between expected and actual"
        failed_count +=1

for tc in test_cases:
    print(f" {tc['id']} | Module: {tc['module']} | Priority: {tc['priority']} | Notes: {tc['notes']} | Expected: {tc['expected']} | Actual: {tc['actual']} → {tc['status']}")


print(f"Total Passed: {passed_count}")
print(f"Total Failed: {failed_count}")
print(f"Total Skipped: {skipped_count}")