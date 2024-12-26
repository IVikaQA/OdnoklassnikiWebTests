#Страница авторизации
import allure
from pages.BasePage import BasePageHelper
#Импорт класса By, который поддерживает разнные способы обращения к элементам страницы
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_BY_QR_CODE = (By.XPATH, '//a[@data-l="t,get_qr"]')
    RESTORE_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    #REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,register"]')
    VK_BUTTON = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//a[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//a[@data-l="t,yandex"]')
    #OTHER_BUTTON = (By.XPATH, '//*[@data-l="t,other"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_BACK_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    PROFILE_RECOVERY_BUTTON = (By.NAME, 'st.go_to_recovery')

class LoginPageHelper(BasePageHelper):
    @allure.step('Создаем экземпляр класса LoginPage')
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    #Функция проверки того,что страница прогрузилась верно:
    #Тоесть проверяем,что элементы, чьи локаторы описаны выше,есть на странице - видимы
    @allure.step('Проверка наличия элементов на странице')
    def check_page(self):
        try:
            with allure.step('Проверяем корректность загрузки страницы'):
                self.attach_screenshot()
            self.find_element(LoginPageLocators.LOGIN_TAB).click()
            self.find_element(LoginPageLocators.QR_TAB)
            self.find_element(LoginPageLocators.LOGIN_FIELD)
            self.find_element(LoginPageLocators.PASSWORD_FIELD)
            self.find_element(LoginPageLocators.LOGIN_BUTTON)
            self.find_element(LoginPageLocators.LOGIN_BY_QR_CODE)
            self.find_element(LoginPageLocators.RESTORE_LINK)
            self.find_element(LoginPageLocators.VK_BUTTON)
            self.find_element(LoginPageLocators.MAIL_BUTTON)
            self.find_element(LoginPageLocators.YANDEX_BUTTON)
            #self.find_element(LoginPageLocators.OTHER_BUTTON)
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise

    #Функция нажатия на кнопку "Войти в Одноклассники"
    @allure.step('Нажимаем на кнопку "Войти в Одноклассники"')
    def click_login(self):
        #В классе,где находится метод click, есть и другие полезные методы работы с элементами формы
        try:
            #Делаем скриншот
            self.attach_screenshot()
            self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        except Exception as e:
            print(f"Ошибка при нажатии на кнопку входа: {e}")
            raise

    #Функция получения текст из элемента
    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        try:
            self.attach_screenshot()
            return self.find_element(LoginPageLocators.ERROR_TEXT).text
        except Exception as e:
            print(f"Ошибка при получении текста ошибки: {e}")
            return None  # Возвращаем None, если текст не удалось получить

    #Функция заполнения поля логина текстом - Вар 1
    @allure.step('Заполняем поле логина на странице авторизации')
    def push_text(self, *value: str):
        try:
            # Объединяем все элементы value в одну строку
            text_to_send = ''.join(value)
            self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text_to_send)
            self.attach_screenshot()
        except Exception as e:
            print(f"Ошибка при вводе текста: {e}")
            raise  # Повторно выбрасываем последнее исключение

    #Функция заполнения поля логина текстом - Вар 2
    @allure.step('Заполняем поле логина')
    def type_login(self, login):
        try:
            self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
            self.attach_screenshot()
        except Exception as e:
            print(f"Ошибка при получении текста ошибки: {e}")
            return None  # Возвращаем None, если текст не удалось получить

    # Функция заполнения поля пароля текстом
    @allure.step('Заполняем поле пароля')
    def type_password(self, password):
        try:
            self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
            self.attach_screenshot()
        except Exception as e:
            print(f"Ошибка при получении текста ошибки: {e}")
            return None  # Возвращаем None, если текст не удалось получить

    #Функция
    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        try:
            self.attach_screenshot()
            self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()
        except Exception as e:
            print(f"Ошибка при получении текста ошибки: {e}")
            return None  # Возвращаем None, если текст не удалось получить

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        try:
            self.attach_screenshot()
            self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()
        except Exception as e:
            print(f"Ошибка при получении текста ошибки: {e}")
            return None  # Возвращаем None, если текст не удалось получить