import allure

from stellar_burger_project.utils.custom_requester import CustomRequester


class IngredientsAPI(CustomRequester):
    """
    Класс для работы с API пользователей.
    """
    INGREDIENTS_PATH = 'ingredients'

    def __init__(self, session):
        super().__init__(session=session)


    @allure.step("Get ingredients")
    def get_ingredients(self, expected_status=200):
        """
        Получение заказа.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="GET",
            endpoint=f'{self.INGREDIENTS_PATH}',
            expected_status=expected_status
        )
