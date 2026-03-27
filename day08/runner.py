from test_data import test_cases
from validator import evaluate_response
from utils import format_output

passed_count = 0
failed_count = 0
skipped_count = 0

for tc in test_cases:
    if not tc["run"]:
        tc["actual"] = None
        tc["status"] = "SKIPPED"
        skipped_count += 1
        continue

    actual_result = evaluate_response(tc["input"])
    tc["actual"] = actual_result

    if actual_result == tc["expected"]:
        tc["status"] = "PASS"
        passed_count += 1
    else:
        tc["status"] = "FAIL"
        failed_count += 1

for tc in test_cases:
    print(format_output(tc))

print(f"\nTotal Passed: {passed_count}")
print(f"Total Failed: {failed_count}")
print(f"Total Skipped: {skipped_count}")