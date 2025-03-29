import allure
import pytest

from stellar_burger_project.data.user import User

@allure.title("Change user data")
class TestChangeUserData:
    @pytest.mark.parametrize("user, expected_status, is_success_change", [
        (User.get_random_user_data(), 200, True),
        (User.get_without_email(), 200, True),
        (User.get_without_name(), 200, True),
        (User.get_without_password(), 200, True),
        (User.get_with_password_only(), 200, True),
        (User.get_with_email_only(), 200, True),
        (User.get_with_name_only(), 200, True)
    ], ids=['Random User Data',
            'Without Email',
            'Without Name',
            'Without Password',
            'With Password Only',
            'With Email Only',
            'With Name Only']
                             )
    def test_change_user_data(self, api_manager, create_and_register_user, user, expected_status, is_success_change):
        response = api_manager.user_api.change_user_data(user.to_json(), expected_status=expected_status)
        response_data = response.json()

        assert response_data['success'] == is_success_change, "User is not changed"
