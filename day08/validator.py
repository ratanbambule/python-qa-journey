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