import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelperHelper

BASE_URL = 'https://ok.ru/'
LOGIN_TEXT = 'email'
PASSWORD_TEXT = '1'

#Тест 1
@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
@allure.feature('Тест Recovery Page')
@allure.story('Негативный:Аутентификация:Не заполняем логин и пароль')
def test_go_to_recovery_after_many_fails(browser):
    #Создается первый объект страницы
    BasePageHelper(browser).get_url(BASE_URL)
    #Создается второй объект страницы
    LoginPage = LoginPageHelper(browser)
    LoginPage.type_login(LOGIN_TEXT)
    #Перебираем значения i от 0 до 2 (1,2,3 = три раза)
    for i in range(3):
        LoginPage.type_password(PASSWORD_TEXT)
        LoginPage.click_login()
    #После клика перехожу на страницу RecoveryPage
    LoginPage.click_recovery()
    #Создается третий объект страницы
    RecoveryPageHelperHelper(browser)
