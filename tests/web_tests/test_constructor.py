import allure
import pytest
from stellar_burger_project.pages.main_page import MainPage

@allure.feature("Конструктор бургера")
class TestConstructorScroll:

    @allure.title("Проверка отображения блока 'Булки'")
    @allure.description("Проверка, что при клике на вкладку 'Булки' отображается соответствующий блок")
    def test_scroll_to_bun_block(self, page):
        main_page = MainPage(page)
        main_page.open()
        main_page.click_filling_button()  # переключаемся сначала на другой блок
        main_page.click_bun_button()
        assert main_page.is_bun_block_visible(), "Блок 'Булки' не отображается"

    @allure.title("Проверка отображения блока 'Соусы'")
    @allure.description("Проверка, что при клике на вкладку 'Соусы' отображается соответствующий блок")
    def test_scroll_to_sauce_block(self, page):
        main_page = MainPage(page)
        main_page.open()
        main_page.click_sauce_button()
        assert main_page.is_sauce_block_visible(), "Блок 'Соусы' не отображается"

    @allure.title("Проверка отображения блока 'Начинки'")
    @allure.description("Проверка, что при клике на вкладку 'Начинки' отображается соответствующий блок")
    def test_scroll_to_filling_block(self, page):
        main_page = MainPage(page)
        main_page.open()
        main_page.click_filling_button()
        assert main_page.is_filling_block_visible(), "Блок 'Начинки' не отображается"