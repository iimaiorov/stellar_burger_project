import allure
import pytest
from stellar_burger_project.data.user_credentials import UserCredentials


@allure.title("Validation of user login")
class TestValidationOfUserLogin:
    @pytest.mark.parametrize("user_credentials_func, expected_status, expected_error_message, is_success_login", [
        (UserCredentials.get_user_authorization_with_email_only, 401, "email or password are incorrect", False),
        (UserCredentials.get_user_authorization_with_password_only, 401, "email or password are incorrect", False),
        (UserCredentials.get_user_authorization_with_only_valid_email, 401, "email or password are incorrect", False),
        (UserCredentials.get_user_authorization_with_only_valid_password, 401, "email or password are incorrect",False),
        (UserCredentials.get_user_authorization_with_empty, 401, "email or password are incorrect", False)
    ], ids=[
        "Email Only",
        "Password Only",
        "Valid Email Only",
        "Valid Password Only",
        "Empty Credentials"
    ])
    def test_validation_of_user_login(self, api_manager, create_and_register_user, user_credentials_func,
                                      expected_status,
                                      expected_error_message, is_success_login):
        user_credentials = user_credentials_func(create_and_register_user)
        response_login = api_manager.user_api.login_user(user_credentials.to_json(), expected_status=expected_status)
        error_message = response_login.json().get('message')

        assert error_message == expected_error_message, "Message is incorrect"
        assert not is_success_login, "User is login"
