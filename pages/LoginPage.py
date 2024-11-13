from pages.BasePage import BasePage
#Импорт класса By, который поддерживает разнные способы обращения к элементам страницы
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_BY_QR_CODE = (By.XPATH, '//a[@data-l="t,get_qr"]')
    RESTORE_LINK = (By.XPATH, '//a[@data-l="t,restore"]')
    #REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-cauth-login-footer"]/a[@data-l="t,register"]')
    VK_BUTTON = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAIL_BUTTON = (By.XPATH, '//a[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//a[@data-l="t,yandex"]')
    OTHER_BUTTON = (By.XPATH, '//*[@data-l="t,other"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    #Функция проверки того,что страница прогрузилась верно:
    #Тоесть проверяем,что элементы, чьи локаторы описаны выше,есть на странице - видимы
    def check_page(self):
        try:
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
            self.find_element(LoginPageLocators.OTHER_BUTTON)
        except Exception as e:
            print(f"Ошибка при проверке страницы: {e}")
            raise

    #Функция нажатия на кнопку "Войти в Одноклассники"
    def click_login(self):
        #В классе,где находится метод click, есть и другие полезные методы работы с элементами формы
        try:
            self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        except Exception as e:
            print(f"Ошибка при нажатии на кнопку входа: {e}")
            raise

    #Функция получения текст из элемента
    def get_error_text(self):
        try:
            return self.find_element(LoginPageLocators.ERROR_TEXT).text
        except Exception as e:
            print(f"Ошибка при получении текста ошибки: {e}")
            return None  # Возвращаем None, если текст не удалось получить

    #Функция заполнения поля текстом
    def push_text(self, *value: str):
        try:
            # Объединяем все элементы value в одну строку
            text_to_send = ''.join(value)
            self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(text_to_send)
        except Exception as e:
            print(f"Ошибка при вводе текста: {e}")
            raise  # Повторно выбрасываем последнее исключение
