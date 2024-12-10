#Страница регистрации
import allure
from pages.BasePage import BasePageHelper
#Импорт класса By, который поддерживает разнные способы обращения к элементам страницы
from selenium.webdriver.common.by import By
import random

class RegistrationPageLocators:
    #Сам список (контейнер)
    COUNTRY_LIST = (By.XPATH,'//div[@data-l="t,country"]')
    #Элемент списка
    COUNTRY_ITEM = (By.XPATH,'//*[@class="country-select_i"]')
    COUNTRY_CODE = (By.XPATH, '//div[@class="country-select_code"]')
    #Поле для ввода телефона
    PHONE_FIELD = (By.XPATH,'//div[@data-l="t,phone"]')
    #Кнопка "Далее"
    SUBMIT_BUTTON = (By.XPATH,'//input[@data-l="t,submit"]')
    #Обратиться в службу поддержки
    SUPPORT_BUTTON = (By.XPATH,'//*[@data-l="t,support"]')

class RegistrationPageHelper(BasePageHelper):
    @allure.step('Создаем экземпляр класса RegistrationPage')
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    # Функция проверки наличия элементов на странице
    @allure.step('Проверка наличия элементов на странице')
    def check_page(self):
        try:
            with allure.step('Проверяем корректность загрузки страницы'):
                self.attach_screenshot()
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)
            self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise

    #Функция выбора элемента из списка, рандомно
    @allure.step('Проверка выбора элемента из спика, рандомно')
    def select_random_country(self):
        try:
            with allure.step('Выбираем рандомно страну'):
                #212 - это колличество элементов в списке выбора на странице
                random_number = random.randint(0,212)
                #Кликаем на список
                self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
                #Загружаем элементы списка
                country_items = self.find_elements(RegistrationPageLocators.COUNTRY_CODE)
            with allure.step('Получаем значение из поля для ввода телефона после выбора страны'):
                #Получаем значение из поля для ввода телефона после выбора страны
                country_code = country_items[random_number].get_attribute("text")
                #Выбираем рандомный элемент из списка
                country_items[random_number].click()
            with allure.step('Возвращаем полученный код страны'):
                return country_code
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise

    #Функция получения значения из поля для ввода телефона после выбора страны
    @allure.step('Проверка получения значения из поля для ввода телефона после выбора страны')
    def get_phone_field_value(self):
        try:
            self.attach_screenshot()
            return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute("value")
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise

