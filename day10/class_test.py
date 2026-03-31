class TestCase:

    def __init__(self, id, module, priority, input, expected):
        self.id = id
        self.module = module
        self.priority = priority
        self.input = input  
        self.expected = expected
        self.actual = None
        self.status = None
        self.notes = None

    def validate_response(self):
        try:
            clean_response = self.input.strip().lower()

            if clean_response == "":
                self.actual = "FAIL"
            elif "error" in clean_response:
                self.actual = "FAIL"
            elif "pricing" in clean_response:
                self.actual = "IMPORTANT"
            elif len(clean_response) <10:
                self.actual = "WARNING"
            else:
                self.actual = "PASS"

        except AttributeError:
            self.actual = "ERROR - response was not a string"
        except Exception as e:
            self.actual = f"ERROR - unexpected issue: {e}"

        if self.actual == self.expected:
            self.status = "PASS"
            self.notes = "Matched expected result"
        else:
            self.status = "FAIL"
            self.notes = f"Expected: {self.expected} | Actual: {self.actual}"

    def report(self):
        print(f"{self.status} | {self.id} | {self.module} | {self.notes} | Expected: {self.expected} | Actual: {self.actual}")
    

tc1 = TestCase("TC-01", "Pricing", "High", "AI helps in pricing", "IMPORTANT")
tc2 = TestCase("TC-02", "Login", "Low", "", "FAIL")
tc3 = TestCase("TC-03", "Logout", "Medium", "System ERROR occurred", "FAIL")
tc4 = TestCase("TC-04", "Pricing", "High", "Ok", "WARNING")
tc5 = TestCase("TC-05", "Login", "Low", "AI improves sales efficiency", "PASS")
tc6 = TestCase("TC-06", "Pricing", "High", None, "ERROR - response was not a string")
tc7 = TestCase("TC-07", "Pricing", "High", 12345, "ERROR - response was not a string")

for tc in [tc1, tc2, tc3, tc4, tc5, tc6, tc7]:
    tc.validate_response()
    tc.report()
