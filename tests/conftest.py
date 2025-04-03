import pytest
import requests
from stellar_burger_project.API.api_manager import ApiManager
from stellar_burger_project.data.user import User


@pytest.fixture(scope='class', autouse=True)
def session():
    """
    Фикстура для создания HTTP-сессии.
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope='class')
def api_manager(session):
    """
    Фикстура для создания экземпляра ApiManager.
    """
    return ApiManager(session)

@pytest.fixture(scope='class')
def create_user():
    user = User.get_random_user_data()
    return user

@pytest.fixture(scope='class')
def create_and_register_user(api_manager,create_user):
    user = create_user
    api_manager.user_api.register_user(user.to_json(), need_logging=False)
    api_manager.user_api.authenticate((user.email, user.password))
    yield user
    api_manager.user_api.delete_user(need_logging=False)

@pytest.fixture(scope='class')
def ingredients(api_manager):
    ingredients = api_manager.ingredients_api.get_ingredients().json()
    return ingredients