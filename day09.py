response = None

try:
    length = len(response)
    print("Length:", length)
except TypeError:
    print("ERROR: Response was None — cannot check length")

print("Script continues here...")


print("--------------------------------")
print("--------------------------------")

def evaluate_response(response):
    try:
        if len(response.strip()) == 0:
            return "FAIL"
        elif "error" in response.lower():
            return "FAIL"
        elif len(response) < 20:
            return "WARNING"
        else:
            return "PASS"
    except AttributeError:
        return "ERROR - response was not a string"
    except Exception as e:
        return f"ERROR - unexpected issue: {e}"


# Test it with different inputs
test_inputs = ["This is a valid response from the AI model", "error found", "", None, 12345]

for item in test_inputs:
    result = evaluate_response(item)
    print(f"Input: {repr(item):45} → {result}")


print("--------------------------------")
print("--------------------------------")

def evaluate_response(response):
    try:
        clean_response = response.strip().lower()
        
        if len(clean_response) == 0:
            return "FAIL"
        elif "error" in clean_response:
            return "FAIL"
        elif len(clean_response) < 20:
            return "WARNING"
        else:
            return "PASS"
    except AttributeError:
        return "ERROR - response was not a string"
    except Exception as e:
        return f"ERROR - unexpected issue: {e}"

test_inputs = ["This is a valid response from the AI model", "error found", "", None, 12345]

for item in test_inputs:
    result = evaluate_response(item)
    print(f"Input: {repr(item):45} → {result}")


print("--------------------------------")
print("--------------------------------")
print("--ALSO ADDED TRY-EXCEPT BLOCK IN VALIDATOR.PY--")