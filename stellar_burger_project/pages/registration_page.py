import allure
from playwright.sync_api import Page, expect


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.input_name = page.locator("//fieldset[1]//input")
        self.input_email = page.locator("//fieldset[2]//input")
        self.input_password = page.locator("//fieldset[3]//input")
        self.reg_button = page.locator("//button[text()='Зарегистрироваться']")
        self.pass_error_message = page.locator("//*[@class='input__error text_type_main-default']")
        self.login_link = page.locator("//a[text()='Войти']")

    @allure.step("Установка значения в поле 'Имя'")
    def set_name(self, name: str):
        self.input_name.fill(name)

    @allure.step("Установка значения в поле 'Email'")
    def set_email(self, email: str):
        self.input_email.fill(email)

    @allure.step("Установка значения в поле 'Пароль'")
    def set_password(self, password: str):
        self.input_password.fill(password)

    @allure.step("Клик на кнопку 'Зарегистрироваться'")
    def click_register(self):
        self.reg_button.click()

    @allure.step("Клик на ссылку 'Войти'")
    def click_login_link(self):
        self.login_link.click()

    @allure.step("Получение текста ошибки под полем пароля")
    def get_password_error_text(self) -> str:
        expect(self.pass_error_message).to_be_visible()
        return self.pass_error_message.text_content()
