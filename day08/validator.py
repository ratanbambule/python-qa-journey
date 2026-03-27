def evaluate_response(response):
    try:
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
    except AttributeError:
        return "ERROR - response was not a string"
    except Exception as e:
        return f"ERROR - unexpected issue: {e}"