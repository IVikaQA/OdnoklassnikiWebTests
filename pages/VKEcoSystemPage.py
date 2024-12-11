#Страница "Сервисы VK"

import allure
from pages.BasePage import BasePageHelper
#Импорт класса By, который поддерживает разнные способы обращения к элементам страницы
from selenium.webdriver.common.by import By
import random

class VKEcoSystemPageLocators:
    #Сам список (контейнер)
    TITLE_LABEL = (By.XPATH,'//h1[@class="title-h2"]')

class VKEcoSystemPageHelper(BasePageHelper):
    @allure.step('Создаем экземпляр класса VKEcoSystemPage')
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    # Функция проверки наличия элементов на странице
    @allure.step('Проверка наличия элементов на странице')
    def check_page(self):
        try:
            with allure.step('Проверяем корректность загрузки страницы'):
                self.attach_screenshot()
            self.find_element(VKEcoSystemPageLocators.TITLE_LABEL)
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise