import allure
from playwright.sync_api import Page



class MainPage:

    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.login_button = page.locator("//button[text()='Войти в аккаунт']")
        self.cabinet_button = page.locator("//*[@href='/account']")
        self.constructor_button = page.locator("//*[text()='Конструктор']")
        self.burger_button = page.locator("//*[@class='AppHeader_header__logo__2D0X2']")
        self.bun_button = page.locator("//span[@class='text text_type_main-default'][text()='Булки']")
        self.sauce_button = page.locator("//span[@class='text text_type_main-default'][text()='Соусы']")
        self.filling_button = page.locator("//span[@class='text text_type_main-default'][text()='Начинки']")
        self.arrange_order_button = page.locator("//button[text()='Оформить заказ']")
        self.burger_block = page.locator("//div/ul[1]")
        self.sauce_block = page.locator("//div/ul[2]")
        self.filling_block = page.locator("//div/ul[3]")

    @allure.step("Открываем главную страницу")
    def open(self):
        self.page.goto('/')

    @allure.step("Кликаем на кнопку 'Войти в аккаунт'")
    def click_login_button(self):
        self.login_button.click()

    @allure.step("Кликаем на кнопку 'Личный кабинет'")
    def click_cabinet_button(self):
        self.cabinet_button.click()

    @allure.step("Кликаем на вкладку 'Булки'")
    def click_bun_button(self):
        self.bun_button.click()

    @allure.step("Кликаем на вкладку 'Соусы'")
    def click_sauce_button(self):
        self.sauce_button.click()

    @allure.step("Кликаем на вкладку 'Начинки'")
    def click_filling_button(self):
        self.filling_button.click()

    @allure.step("Проверяем, что кнопка 'Оформить заказ' отображается")
    def is_arrange_order_button_visible(self) -> bool:
        return self.arrange_order_button.is_visible()

    @allure.step("Проверяем, что блок 'Булки' отображается")
    def is_bun_block_visible(self) -> bool:
        return self.burger_block.is_visible()

    @allure.step("Проверяем, что блок 'Соусы' отображается")
    def is_sauce_block_visible(self) -> bool:
        return self.sauce_block.is_visible()

    @allure.step("Проверяем, что блок 'Начинки' отображается")
    def is_filling_block_visible(self) -> bool:
        return self.filling_block.is_visible()
