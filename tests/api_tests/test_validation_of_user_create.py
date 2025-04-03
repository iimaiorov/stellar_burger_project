import allure
import pytest
from stellar_burger_project.data.user import User

@allure.feature("Validation of user create")
class TestValidationOfUserCreate:
    @allure.title("Validation of user create")
    @pytest.mark.api
    @pytest.mark.parametrize("user, expected_status, expected_error_message", [
        (User.get_without_email(), 403, "Email, password and name are required fields"),
        (User.get_without_name(), 403, "Email, password and name are required fields"),
        (User.get_without_password(), 403, "Email, password and name are required fields"),
        (User.get_with_password_only(), 403, "Email, password and name are required fields"),
        (User.get_with_email_only(), 403, "Email, password and name are required fields"),
        (User.get_with_name_only(), 403, "Email, password and name are required fields"),
        (User.get_empty(), 403, "Email, password and name are required fields")
    ], ids=[
        "Without Email",
        "Without Name",
        "Without Password",
        "With Password Only",
        "With Email Only",
        "With Name Only",
        "Empty"])
    def test_validation_of_user_create(self, api_manager, user, expected_status, expected_error_message):
        user_data = user.to_json()
        response = api_manager.user_api.register_user(user_data, expected_status=expected_status)
        response_data = response.json()
        assert response.status_code == expected_status, "Status code is incorrect"
        assert response_data['message'] == expected_error_message, "Message is incorrect"
