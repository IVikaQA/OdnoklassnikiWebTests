#Страница

import allure
from pages.BasePage import BasePageHelper
#Импорт класса By, который поддерживает разнные способы обращения к элементам страницы
from selenium.webdriver.common.by import By

class AdvertisementCabinetHelpLocators:
    TITLE = (By.XPATH, '//span[text()="Рекламный кабинет"]')

class AdvertisementCabinetHelpHelper(BasePageHelper):
    @allure.step('Создаем экземпляр класса AdvertisementCabinetHelpPage')
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    # Функция проверки наличия элементов на странице
    @allure.step('Проверка наличия элементов на странице')
    def check_page(self):
        try:
            with allure.step('Проверяем корректность загрузки страницы'):
                self.attach_screenshot()
            self.find_element(AdvertisementCabinetHelpLocators.TITLE)
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise