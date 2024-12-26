from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VKEcoSystemPage import VKEcoSystemPageHelper
import allure

BASE_URL = "https://ok.ru/"

#Тест 1
@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
@allure.feature('Тест VKEcoSystemPage')
@allure.story('Позитивный:Возвращение на главную страницу со страницы экосистемы VK')
def test_open_vk_ecosystem(browser):
    #1. Инициализация страницы: Вызывается конструктор класса-родителя BasePage, который,
    # содержит общие методы для работы со страницами. Сейчас вызывается метод get_url(BASE_URL),
    # который открывает указанный URL (в данном случае, базовый URL для страницы авторизации).
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    #2. Создается экземпляр класса LoginPageHelper, который содержит методы для взаимодействия
    # с элементами на странице логина.
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_windows_id(0)
    LoginPage.click_vk_ecosystem()
    LoginPage.click_more_button()
    new_window_id = LoginPage.get_windows_id(1)
    LoginPage.switch_window(new_window_id)
    # 3. Создается экземпляр класса VKEcoSystemHelper
    VKEcoSystemPage = VKEcoSystemPageHelper(browser)
    VKEcoSystemPage.switch_window(current_window_id)
    LoginPageHelper(browser)