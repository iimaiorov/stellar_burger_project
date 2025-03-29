import allure

from stellar_burger_project.data.user import User

@allure.title("Create user")
class TestCreateUser:
    def test_check_user_created(self, api_manager):
        user = User.get_random_user_data().to_json()
        response = api_manager.user_api.register_user(user)
        response_data = response.json()

        assert response_data is not None
        assert response_data['user']['email'] == user['email']

    def test_duplicate_user_can_not_be_created(self, api_manager):
        user = User.get_random_user_data().to_json()
        api_manager.user_api.register_user(user)
        response = api_manager.user_api.register_user(user, expected_status=403)
        response_data = response.json()

        assert response_data['message'] == 'User already exists'
