import allure
from stellar_burger_project.utils.custom_requester import CustomRequester


class OrderAPI(CustomRequester):
    """
    Класс для работы с API пользователей.
    """
    ORDER_PATH = 'orders'

    def __init__(self, session):
        super().__init__(session=session)


    @allure.step("Create a order")
    def create_order(self, order, expected_status=200):
        """
        Создания заказа.
        :param order: Данные заказа.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="POST",
            endpoint=f'{self.ORDER_PATH}',
            data=order,
            expected_status=expected_status
        )

    @allure.step("Get order")
    def get_order(self, expected_status=200):
        """
        Получение заказа.
        :param expected_status: Ожидаемый статус-код.
        """
        return self.send_request(
            method="GET",
            endpoint=f'{self.ORDER_PATH}',
            expected_status=expected_status
        )


