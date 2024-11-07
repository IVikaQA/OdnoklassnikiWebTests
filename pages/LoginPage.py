from pages.BasePage import BasePage
#Импорт класса By, который поддерживает разнные способы обращения к элементам страницы
from selenium.webdriver.common.by import By

class LoginPageLocators:
    ENTER_VKLADKA = (By.XPATH, '//a[@data-l="t,login_tab"]')
    QR_VKLADKA = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    # Вариант 1: //*[@data-l="t,sign_in"]
    LOGIN_BUTTON = (By.XPATH, '//input[@value="Войти в Одноклассники"]')  # Вариант 2
    QR_LOGIN_BUTTON = (By.XPATH, '//a[@aria-label="Войти по QR-коду"]')
    CAN_NOT_LOGIN_SSYLKA = (By.XPATH, '//a[@tsid="restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//a[text()="Зарегистрироваться"]')
    ENTER_ID_VK_BUTTON = (By.XPATH, '//div[@class="soc-login_buttons-container"]/a[1]')
    ENTER_EMAIL_BUTTON = (By.XPATH, '//div[@class="soc-login_buttons-container"]/a[2]')
    ENTER_YANDEX_BUTTON = (By.XPATH, '//div[@class="soc-login_buttons-container"]/a[3]')
    ANOTHER_ENTER_BUTTON = (By.XPATH, '//*[@data-l="t,other"]')

class LoginPageHelper(BasePage):
    pass
