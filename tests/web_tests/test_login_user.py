import allure
import pytest

from stellar_burger_project.pages.main_page import MainPage
from stellar_burger_project.pages.login_page import LoginPage


@allure.feature("Логин пользователя")
class TestLoginUser:
    @pytest.mark.web
    @allure.title("Логин пользователя. Кнопка 'Войти в аккаунт'")
    @allure.description("Логин пользователя с корректными данными")
    def test_login_with_login_button(self, page, create_and_register_user):
        with allure.step('Открытие главной страницы'):
            main_page = MainPage(page)
            main_page.open()

        with allure.step('Переход на страницу логина'):
            main_page.click_login_button()
            login_page = LoginPage(page)

        with allure.step('Логин пользователя с корректными данными'):
            login_page.set_email(create_and_register_user.email)
            login_page.set_password(create_and_register_user.password)
            login_page.click_login()

            assert main_page.is_arrange_order_button_visible

    @pytest.mark.web
    @allure.title("Логин пользователя. Кнопка 'Личный кабинет'")
    @allure.description("Логин пользователя с корректными данными")
    def test_login_with_cabinet_button(self, page, create_and_register_user):
        with allure.step('Открытие главной страницы'):
            main_page = MainPage(page)
            main_page.open()

        with allure.step('Переход на страницу Личного кабинета'):
            main_page.click_cabinet_button()
            login_page = LoginPage(page)

        with allure.step('Логин пользователя с корректными данными'):
            login_page.set_email(create_and_register_user.email)
            login_page.set_password(create_and_register_user.password)
            login_page.click_login()

            assert main_page.is_arrange_order_button_visible



