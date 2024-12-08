import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper,HelpPageLocators
from pages.AdvertisementCabinetHelpPage import AdvertisementCabinetHelpHelper

BASE_URL = "https://ok.ru/help"

#Тест 1
@allure.suite('Проверка страницы помощи')
@allure.title('Проверка вкладки "Рекламный кабинет"')
@allure.feature('Тест Help Page')
@allure.story('Позитивный:Открытие вкладки "Рекламный кабинет"')
def test_help_test(browser):
    #Открываем адрес
    BasePageHelper(browser).get_url(BASE_URL)
    #Создааем объект страницы
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToItem(HelpPageLocators.ADVERTISEMENT_CABINET)
    #Создаем объект класса:Вызывается конструктор класса и последовательно функция check_page
    AdvertisementCabinetHelpHelper(browser)