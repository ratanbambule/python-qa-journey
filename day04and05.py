responses = ["Anyteam is a sales enablement platform", "", "Found 404 ERROR while processing the request", " Anyteam sales has increased the revenue by 10%", "Anyteam", " "]

for response in responses:
    
    if response.strip() == "":
        print("FAIL - response is empty")
    elif "error" in response.lower():
        print("FAIL - response contains error")
    elif "increased the revenue" in response.lower():
        print("IMPROTANT")
    elif len(response) < 10:
        print("WARNING - response is too short")
    else:
        print("PASS - response is valid")


print("--------------------------------")
response = "  ERROR  "

if response.strip().lower() == "error":
    print("FAIL - response contains error")
else:
    print("PASS - response does not contain error")