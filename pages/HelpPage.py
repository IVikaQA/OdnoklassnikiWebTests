#Страница помощи
from selenium.webdriver import ActionChains
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY = (By.XPATH, '//a[contains(@href, "segodnya-aktualno")]')
    REGISTRATION = (By.XPATH, '//a[contains(@href, "registraciya")]')
    MY_PROFILE = (By.XPATH, '//a[contains(@href, "moi-profil")]')
    COMMUNICATION = (By.XPATH, '//a[contains(@href, "obshchenie")]')
    PROFILE_ACCESS = (By.XPATH, '//a[contains(@href, "dostup-k-profilu")]')
    SECURITY = (By.XPATH, '//a[contains(@href, "bezopasnost")]')
    GROUPS = (By.XPATH, '//a[contains(@href, "gruppy")]')
    PAYED_FUNCTIONS = (By.XPATH, '//a[contains(@href, "platnye-funkcii")]')
    SPAM = (By.XPATH, '//a[contains(@href, "narusheniya-i-spam")]')
    GAMES_AND_APPS = (By.XPATH, '//a[contains(@href, "igry-i-prilojeniya")]')
    OTHER_SERVICES = (By.XPATH, '//a[contains(@href, "drugie-servisy")]')
    IMPORTANT_INFORMATION = (By.XPATH, '//a[contains(@href, "poleznaya-informaciya")]')
    ADVERTISEMENT_CABINET = (By.XPATH, '//a[contains(@href, "reklamnyi-kabinet")]')

class HelpPageHelperHelper(BasePageHelper):
    @allure.step('Создаем экземпляр класса HelpPage')
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    # Функция проверки наличия элементов на странице
    @allure.step('Проверка наличия элементов на странице')
    def check_page(self):
        try:
            with allure.step('Проверяем корректность загрузки страницы'):
                self.attach_screenshot()
            self.find_element(HelpPageLocators.SPAM)
            self.find_element(HelpPageLocators.GROUPS)
            self.find_element(HelpPageLocators.MY_PROFILE)
            self.find_element(HelpPageLocators.SECURITY)
            self.find_element(HelpPageLocators.ACTUAL_TODAY)
            self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)
            self.find_element(HelpPageLocators.COMMUNICATION)
            self.find_element(HelpPageLocators.SECURITY)
            self.find_element(HelpPageLocators.GAMES_AND_APPS)
            self.find_element(HelpPageLocators.IMPORTANT_INFORMATION)
            self.find_element(HelpPageLocators.OTHER_SERVICES)
            self.find_element(HelpPageLocators.PAYED_FUNCTIONS)
            self.find_element(HelpPageLocators.REGISTRATION)
            self.find_element(HelpPageLocators.SEARCH_FIELD)
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise

    # Функция скрола до элемента на странице
    @allure.step('Скролим до элемента на странице и кликаем на него')
    def scrollToItem(self,locator):
        try:
            scroll_item = self.find_element(locator)
            #В классе ActionChains есть и другие полезные методы,помимо скрола
            #Набираем действия: 1)Скроллим 2)Кликаем 3)Выполняем perfom (обязательно)
            ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()
        except Exception as e:
            print(f"Ошибка при получении текста ошибки: {e}")
            return None  # Возвращаем None, если текст не удалось получить