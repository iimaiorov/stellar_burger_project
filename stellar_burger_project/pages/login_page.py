import allure
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.input_email = page.locator("//input[@name='name']")
        self.input_password = page.locator("//input[@name='Пароль']")
        self.login_button = page.locator("//button[text()='Войти']")
        self.login_link = page.locator("//a[text()='Войти']")
        self.register_link = page.locator("//a[text()='Зарегистрироваться']")
        self.reset_password_link = page.locator("//a[text()='Восстановить пароль']")
        self.burger_button = page.locator("//*[@class='AppHeader_header__logo__2D0X2']")
        self.constructor_button = page.locator("//*[text()='Конструктор']")
        self.exit_button = page.locator("//button[text()='Выход']")

    @allure.step("Ввод Email")
    def set_email(self, email: str):
        self.input_email.click()
        self.input_email.fill(email)

    @allure.step("Ввод пароля")
    def set_password(self, password: str):
        self.input_password.click()
        self.input_password.fill(password)

    @allure.step("Клик на кнопку 'Войти'")
    def click_login(self):
        self.login_button.click()

    @allure.step("Клик на ссылку 'Зарегистрироваться'")
    def click_register_link(self):
        self.register_link.click()

    @allure.step("Клик на ссылку 'Войти'")
    def click_login_link(self):
        self.login_link.click()

    @allure.step("Клик на ссылку 'Восстановить пароль'")
    def click_reset_password_link(self):
        self.reset_password_link.scroll_into_view_if_needed()
        self.reset_password_link.click()

    @allure.step("Клик на кнопку 'Конструктор'")
    def click_constructor(self):
        self.constructor_button.click()

    @allure.step("Клик на логотип 'Stellar Burger'")
    def click_burger_logo(self):
        self.burger_button.click()

    @allure.step("Клик на кнопку 'Выход'")
    def click_logout(self):
        self.exit_button.click()