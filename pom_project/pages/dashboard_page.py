class DashboardPage:
    """
    Represents the Dashboard page after successful login.
    Holds all locators and actions for the main dashboard.
    """

    def __init__(self, username):
        self.url              = "https://app.anyteam.ai/dashboard"
        self.welcome_banner   = "div.welcome-message"
        self.nav_menu         = "nav.sidebar"
        self.account_research = "section#account-research"
        self.ask_ai_button    = "button#ask-ai"
        self.logout_button    = "a#logout"

        # Simulated state
        self._username = username
        self._current_tab = "Home"

    def get_welcome_message(self):
        """Returns the welcome message shown after login"""
        return f"Welcome back, {self._username}!"

    def navigate_to(self, tab_name):
        """Click a navigation tab in the sidebar"""
        valid_tabs = ["Home", "Account Research", "Ask AI", "Settings", "Contacts"]

        if tab_name not in valid_tabs:
            print(f"  [DashboardPage] ERROR: '{tab_name}' is not a valid tab")
            return False

        self._current_tab = tab_name
        print(f"  [DashboardPage] Navigated to: {tab_name}")
        return True

    def get_current_tab(self):
        """Returns the name of the currently active tab"""
        return self._current_tab

    def click_ask_ai(self):
        """Click the Ask AI button"""
        self.navigate_to("Ask AI")
        print(f"  [DashboardPage] Ask AI panel opened")

    def is_loaded(self):
        """Verify the dashboard has loaded correctly"""
        return self._username is not None and len(self._username) > 0

    def logout(self):
        """Click logout and return to login page"""
        print(f"  [DashboardPage] Logging out: {self._username}")
        self._username = None