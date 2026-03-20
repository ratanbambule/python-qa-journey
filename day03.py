actual = "Login Successful"
expected = "Login Failed"

if actual == expected:
    print("Test Passed")
else:
    print("Test Failed")


faithfulness = 0.95
threshold = 0.75

if faithfulness >= threshold:
    print("✅ LLM Quality PASS: Score", faithfulness, "is above threshold")
else:
    print("❌ LLM Quality FAIL: Score", faithfulness, "is below threshold", threshold)


faithfulness = 0.70

if faithfulness >= 0.80:
    print("✅ PASS — High quality output")
elif faithfulness >= 0.60:
    print("⚠️  WARNING — Acceptable but needs review")
else:
    print("❌ FAIL — LLM output below minimum threshold")