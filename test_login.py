import pytest
from pages.login_page import LoginPage


class TestLogin:
    """Test suite for login functionality."""

    def test_valid_login(self, page):
        """Verify that a valid user can log in successfully."""
        login_page = LoginPage(page)
        login_page.open().login("standard_user", "secret_sauce")
        assert login_page.is_logged_in(), "User should be logged in after valid credentials"

    def test_invalid_password(self, page):
        """Verify that an invalid password shows an error message."""
        login_page = LoginPage(page)
        login_page.open().login("standard_user", "wrong_password")
        error = login_page.get_error_message()
        assert "Username and password do not match" in error

    def test_empty_username(self, page):
        """Verify that empty username shows a validation error."""
        login_page = LoginPage(page)
        login_page.open().login("", "secret_sauce")
        error = login_page.get_error_message()
        assert "Username is required" in error

    def test_locked_out_user(self, page):
        """Verify that a locked-out user sees an appropriate error."""
        login_page = LoginPage(page)
        login_page.open().login("locked_out_user", "secret_sauce")
        error = login_page.get_error_message()
        assert "locked out" in error.lower()

    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("invalid_user", "secret_sauce", "Username and password do not match"),
    ])
    def test_login_validations(self, page, username, password, expected_error):
        """Data-driven test for multiple login validation scenarios."""
        login_page = LoginPage(page)
        login_page.open().login(username, password)
        error = login_page.get_error_message()
        assert expected_error in error, f"Expected '{expected_error}' in error message, got: '{error}'"
