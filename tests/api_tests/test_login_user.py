import allure
import pytest

from stellar_burger_project.data.user_credentials import UserCredentials

@allure.feature("Login user")
class TestLoginUser:
    @allure.title("Login user")
    @pytest.mark.api
    def test_check_user_can_be_login(self, api_manager, create_and_register_user):
        response_login = api_manager.user_api.login_user(UserCredentials.from_user(create_and_register_user).to_json())
        is_user_login = response_login.json().get('success')
        assert is_user_login, "User is not logged in"
