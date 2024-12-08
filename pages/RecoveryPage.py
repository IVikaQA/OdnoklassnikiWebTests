#Страница восстановления профиля
import allure
from pages.BasePage import BasePageHelper
#Импорт класса By, который поддерживает разнные способы обращения к элементам страницы
from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH,'//*[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH,'//*[@data-l="t,email"]')
    QR_CODE = (By.XPATH,'//*[@class="qr_code_image"]')
    SUPPORT_BUTTON = (By.XPATH,'//*[@data-l="t,support"]')

class RecoveryPageHelperHelper(BasePageHelper):
    @allure.step('Создаем экземпляр класса RecoveryPage')
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    # Функция проверки наличия элементов на странице
    @allure.step('Проверка наличия элементов на странице')
    def check_page(self):
        try:
            with allure.step('Проверяем корректность загрузки страницы'):
                self.attach_screenshot()
            self.find_element(RecoveryPageLocators.PHONE_BUTTON)
            self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
            self.find_element(RecoveryPageLocators.QR_CODE)
            self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise