test_cases = [
    {"id": "TC-01", "module": "Pricing", "priority": "High", "input": "AI helps in pricing", "expected": "IMPORTANT", "run": True},
    {"id": "TC-02", "module": "Login", "priority": "Low", "input": "", "expected": "FAIL", "run": False},
    {"id": "TC-03", "module": "Logout", "priority": "Medium", "input": "System ERROR occurred", "expected": "FAIL", "run": False},
    {"id": "TC-04", "module": "Pricing", "priority": "High", "input": "Ok", "expected": "WARNING", "run": True},
    {"id": "TC-05", "module": "Login", "priority": "Low", "input": "AI improves sales efficiency", "expected": "PASS", "run": True}
]