import allure
from stellar_burger_project.utils.custom_requester import CustomRequester


class UserAPI(CustomRequester):
    """
    Класс для работы с API пользователей.
    """
    USER_PATH = 'auth/'

    def __init__(self, session):
        super().__init__(session=session)


    @allure.step("Create user")
    def register_user(self, user_data, expected_status=200):
        """
        Регистрация нового пользователя.
        :param user_data: Данные пользователя.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="POST",
            endpoint=f'{self.USER_PATH}register',
            data=user_data,
            expected_status=expected_status
        )

    @allure.step("Delete client")
    def delete_user(self, expected_status=202):
        """
        Удаление пользователя
        :param expected_status:
        """
        return self.send_request(
            method="DELETE",
            endpoint=f'{self.USER_PATH}user',
            expected_status=expected_status
        )

    @allure.step("Login of a user")
    def login_user(self, user_data, expected_status=200):
        """
        Вход пользователя
        :param user_data:
        :param expected_status:
        """
        return self.send_request(
            method="POST",
            endpoint=f'{self.USER_PATH}login',
            data=user_data,
            expected_status=expected_status
        )

    @allure.step("Change user data")
    def change_user_data(self, user_data, expected_status=200):
        """
        Изменение данных пользователя
        :param user_data:
        :param expected_status:
        """
        return self.send_request(
            method="PATCH",
            endpoint=f'{self.USER_PATH}user',
            data=user_data,
            expected_status=expected_status
        )

    def authenticate(self, user_creds):
        login_data = {
            "email": user_creds[0],
            "password": user_creds[1]
        }

        response = self.login_user(login_data).json()
        if "accessToken" not in response:
            raise KeyError("token is missing")

        token = response["accessToken"]
        self._update_session_headers(**{"authorization": token})




