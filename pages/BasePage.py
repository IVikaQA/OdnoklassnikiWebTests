# Родитель-страница для наших страниц
# Здесь опишем, то как мы будем искать элементы на странице +
# метод,которым будут пользоваться предки
import allure
# Вызываем класс-задержку для WebDriver.
# Например,кликнули на кнопку и ждем появление всплывающего окна 7 сек
from selenium.webdriver.support.wait import WebDriverWait
# Вызываем класс-описатель: как ждать ?
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePageLocators:
    # Левый верхний угол:OK
    LOGO_BUTTON = (By.ID, 'nohook_logo_link')
    # Правый верхний угол: КУБИК из точек
    VK_ECOSYSTEM_BUTTON = (By.XPATH, '//*[@data-l="t,vk_ecosystem"]')
    # Кнопка "Еще", после кубика из точек
    MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')


class BasePageHelper:
    # Конструктор класс
    @allure.step('Создаем экземпляр класса BasePage')
    def __init__(self, driver):
        # Здесь происходит присвоение значение параметра driver атрибуту self.driver
        # экземпляра класса BasePage
        with allure.step('Открываем форму авторизации'):
            self.driver = driver

    # Функция проверки наличия элементов на странице
    @allure.step('Проверка наличия элементов на странице')
    def check_page(self):
        try:
            with allure.step('Проверяем корректность загрузки страницы'):
                self.attach_screenshot()
            self.find_element(BasePageLocators.LOGO_BUTTON)
            self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON)
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise

    # Функция поиска элементов на странице
    @allure.step('Ищем элемент на странице')
    def find_element(self, locator, time=5):
        try:
            # Мы создаем объект и потом возращаем его,в котором передаем драйвер и время,которое драйверу нужно ждать
            # Драйвер подожди (until) пока элемент на странице станет видимым
            # Алгоритм работы функции
            # 1.Передаем в функцию локатор
            # 2.Ждем,что элемент стал видимым - 5 сек
            # 3.Возвращаем элемент класса WebElement (Значит доступны метожды работы класса WebElement)
            return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),message=f"Не удалось найти элемент {locator}")
        except Exception as e:
            print(f"Ошибка: {e}")
            raise

    # Функция поиска элемента в выпадающем списке
    @allure.step('Ищем элемент в выпадающем списке')
    def find_elements(self, locator, time=5):
        try:
            return WebDriverWait(self.driver, time).until(
                expected_conditions.visibility_of_all_elements_located(locator),
                message=f"Не удалось найти элементы {locator}")
        except Exception as e:
            print(f"Ошибка: {e}")
            raise

    # Функция перехода по URL
    @allure.step('Открываем главную страницу ok.ru')
    def get_url(self, url):
        try:
            return self.driver.get(url)
        except Exception as e:
            print(f"Ошибка: {e}")
        raise

    # Функция делает скриншот экрана
    @allure.step('Делаем скриншот')
    def attach_screenshot(self):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)
        except Exception as e:
            print(f"Ошибка: {e}")
            raise

    # Функция кликает на элемент "Еще"
    @allure.step('Нажимаем на кнопку экосистемы')
    def click_vk_ecosystem(self):
        try:
         self.find_element(BasePageLocators.VK_ECOSYSTEM_BUTTON).click()
        except Exception as e:
            print(f"Ошибка: {e}")
            raise

    # Функция кликаает на кнопку "Еще"
    @allure.step('Нажимаем на кнопку "Еще"')
    def click_more_button(self):
        try:
            self.find_element(BasePageLocators.MORE_BUTTON).click()
            # После клика перенаправялемся на слудующую вкладку
        except Exception as e:
            print(f"Ошибка: {e}")
            raise

    # Функция получения 'id' страницы
    @allure.step('Получаем "id" страницы')
    def get_windows_id(self, index):
        # Передавая ноль - это значит первая страница, потом 1 - вторая вкладка
        return self.driver.window_handles[index]

    # Функция переключения на страницу
    @allure.step('Переходим на страницу')
    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)