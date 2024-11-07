from pages.BasePage import BasePage
#Импорт класса By, который поддерживает разнные способы обращения к элементам страницы
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    # Вариант 2: //input[@value="Войти в Одноклассники"]'
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]') #Вариант 1

class LoginPageHelper(BasePage):
    pass
