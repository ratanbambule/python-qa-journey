import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def run_test(name, passed, notes=""):
    status = "PASS" if passed else "FAIL"
    print(f"\n[{status}] {name}")
    if notes:
        print(f"       {notes}")


print("=" * 55)
print("LOGIN FLOW — Page Object Model Tests")
print("=" * 55)


# ── Test 1: Valid login ──────────────────────────────────
print("\n--- TC-01: Valid credentials ---")
login = LoginPage()
login.login("ratan@anyteam.ai", "secure123")
run_test(
    "Valid login succeeds",
    login.is_login_successful()
)

# ── Test 2: Dashboard loads after login ──────────────────
print("\n--- TC-02: Dashboard loads after login ---")
dashboard = DashboardPage("Ratan")
run_test(
    "Dashboard is loaded",
    dashboard.is_loaded(),
    f"Welcome message: {dashboard.get_welcome_message()}"
)

# ── Test 3: Navigation works ─────────────────────────────
print("\n--- TC-03: Navigate to Account Research ---")
result = dashboard.navigate_to("Account Research")
run_test(
    "Navigation to Account Research",
    result and dashboard.get_current_tab() == "Account Research"
)

# ── Test 4: Invalid tab navigation ───────────────────────
print("\n--- TC-04: Navigate to invalid tab ---")
result = dashboard.navigate_to("Billing")
run_test(
    "Invalid tab returns False",
    result == False,
    "Expected False for non-existent tab"
)

# ── Test 5: Empty email ──────────────────────────────────
print("\n--- TC-05: Login with empty email ---")
login2 = LoginPage()
login2.login("", "secure123")
run_test(
    "Empty email shows error",
    not login2.is_login_successful(),
    f"Error: {login2.get_error_message()}"
)

# ── Test 6: Invalid email format ─────────────────────────
print("\n--- TC-06: Login with invalid email format ---")
login3 = LoginPage()
login3.login("notanemail", "secure123")
run_test(
    "Invalid email format caught",
    not login3.is_login_successful(),
    f"Error: {login3.get_error_message()}"
)

# ── Test 7: Short password ───────────────────────────────
print("\n--- TC-07: Login with short password ---")
login4 = LoginPage()
login4.login("ratan@anyteam.ai", "abc")
run_test(
    "Short password caught",
    not login4.is_login_successful(),
    f"Error: {login4.get_error_message()}"
)

# ── Test 8: Logout ───────────────────────────────────────
print("\n--- TC-08: Logout ---")
dashboard.logout()
run_test(
    "Logout clears session",
    not dashboard.is_loaded()
)

print("\n" + "=" * 55)
print("ALL TESTS COMPLETE")
print("=" * 55)
