from stellar_burger_project.API.ingredients_api import IngredientsAPI
from stellar_burger_project.API.order_api import OrderAPI
from stellar_burger_project.API.user_api import UserAPI

class ApiManager:
    """
    Класс для управления API-классами с единой HTTP-сессией.
    """

    def __init__(self, session):
        """
        Инициализация ApiManager.
        :param session: HTTP-сессия, используемая всеми API-классами.
        """
        self.session = session
        self.user_api = UserAPI(session)
        self.order_api = OrderAPI(session)
        self.ingredients_api = IngredientsAPI(session)