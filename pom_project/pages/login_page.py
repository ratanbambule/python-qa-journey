class LoginPage:
    """
    Represents the Login page of Anyteam.
    Holds all locators and actions for this page.
    No test logic here — only page behaviour.
    """

    def __init__(self):
        # These are the locators (what you would inspect in browser)
        # In real Selenium: driver.find_element(By.ID, "email")
        # For now we simulate the page with a dictionary
        self.url             = "https://app.anyteam.ai/login"
        self.email_field     = "input#email"
        self.password_field  = "input#password"
        self.login_button    = "button[type='submit']"
        self.error_message   = "div.error-message"

        # Simulated page state
        self._fields = {}

    def enter_email(self, email):
        """Type email into the email field"""
        self._fields["email"] = email
        print(f"  [LoginPage] Entered email: {email}")

    def enter_password(self, password):
        """Type password into the password field"""
        self._fields["password"] = password
        print(f"  [LoginPage] Entered password: {'*' * len(password)}")

    def click_login(self):
        """Click the login/submit button"""
        print(f"  [LoginPage] Clicked login button")

    def login(self, email, password):
        """
        Full login action — combines all steps.
        This is what tests will call most of the time.
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Returns the error message shown on failed login"""
        # Simulated — in real Selenium this reads from the DOM
        email = self._fields.get("email", "")
        password = self._fields.get("password", "")

        if not email:
            return "Email is required"
        if "@" not in email:
            return "Invalid email format"
        if not password:
            return "Password is required"
        if len(password) < 6:
            return "Password too short"
        return None   # No error = login successful

    def is_login_successful(self):
        """Returns True if no error messages are shown"""
        return self.get_error_message() is None