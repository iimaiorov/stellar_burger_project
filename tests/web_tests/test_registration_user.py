import allure
import faker
import pytest

from stellar_burger_project.pages.main_page import MainPage
from stellar_burger_project.pages.login_page import LoginPage
from stellar_burger_project.pages.registration_page import RegistrationPage


@allure.feature("Регистрация пользователя")
class TestRegistrationUser:

    @pytest.mark.web
    @allure.title("Регистрация нового пользователя")
    @allure.description("Регистрация нового пользователя с корректными данными")
    def test_check_user_can_be_registered(self, page, create_user):
        with allure.step('Открытие главной страницы'):
            main_page = MainPage(page)
            main_page.open()

        with allure.step('Переход на страницу регистрации'):
            main_page.click_login_button()
            login_page = LoginPage(page)
            login_page.click_register_link()
            registration_page = RegistrationPage(page)

        with allure.step('Регистрация пользователя'):
            registration_page.set_email(create_user.email)
            registration_page.set_password(create_user.password)
            registration_page.set_name(create_user.name)
            registration_page.click_register()

            assert main_page.is_arrange_order_button_visible

    @pytest.mark.web
    @allure.title("Регистрация пользователя с коротким паролем")
    @allure.description("Регистрация пользователя с паролем, содержащим менее 6 символов")
    def test_check_user_can_not_be_registered_with_short_password(self, page, create_user):
        user = create_user
        user.set_password(faker.Faker().password(length=5))
        with allure.step('Открытие главной страницы'):
            main_page = MainPage(page)
            main_page.open()

        with allure.step('Переход на страницу регистрации'):
            main_page.click_login_button()
            login_page = LoginPage(page)
            login_page.click_register_link()

        with allure.step('Регистрация пользователя с коротким паролем'):
            registration_page = RegistrationPage(page)
            registration_page.set_email(create_user.email)
            registration_page.set_password('12345')
            registration_page.set_name(create_user.name)
            registration_page.click_register()

            assert registration_page.get_password_error_text() == "Некорректный пароль"
