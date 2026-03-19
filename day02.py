# day2 - variables
# Every test case has data. Variables store that data.
# Variables are used to store data that can be used in the test case.

# --- Test Case Data (like your Excel test sheet) ---

test_case_id = "TC-001"
module = "Login"
username = "admin@nurix.ai"
password = "Test@1234"
expected = "Dashboard"
actual = "Dahsboard"
status = "not_run"

# --- Print the test case like a report ---
print("Test Case ID:", test_case_id)
print("Module:", module)
print("User name:", username)
print("Password:",password)
print("Expected:",expected)
print("Actual:",actual)
print("Status:",status)

# --- This is what a Ragas eval variable looks like ---
# You will use these exact variables in Month 3

question = "What did AI summarise about TechCorp account?"
actual_answer = "TechCorp is a company that sells technology products and services."
expected_answer = "TechCorp is a company that sells technology products and services."
faithfulness = 0.91
is_hallucination = False

print("----LLM Eval Data----")
print("Question:", question)
print("Actual Answer:", actual_answer)
print("Expected Answer:", expected_answer)
print("Faithfulness:", faithfulness)
print("Is Hallucination:", is_hallucination)

print("--------------------")
print("Home Work")
print("--------------------")

test_case_id = "TC-002"
feature_name = "Call Transcript Summary"
ai_output = "mentioned about greetings, weather, and traffic"
expected_output = "mentioned about greetings, and weather"
score = 0.78
is_correct = True

print("Test Case ID:", test_case_id)
print("Feature Name:", feature_name)
print("AI Output:", ai_output)
print("Expected Output:", expected_output)
print("Score:", score)
print("Is Correct:", is_correct)

print("--------------------")

