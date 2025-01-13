from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
import allure

from tests.test_Recovery import LOGIN_TEXT

BASE_URL = "https://ok.ru/"
LOGIN_TEXT
EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"
WRONG_PASSWORD = '1'

#Тест 1
@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
@allure.feature('Тест Login Page')
@allure.story('Негативный:Аутентификация:Не заполняем логин и пароль')
def test_empty_login_and_password(browser):
    #1.Инициализация страницы: Вызывается конструктор класса-родителя BasePage, который,
    # содержит общие методы для работы со страницами. Сейчас вызывается метод get_url(BASE_URL),
    # который открывает указанный URL (в данном случае, базовый URL для страницы авторизации).
    BasePageHelper(browser).get_url(BASE_URL)
    #2. Создается экземпляр класса LoginPageHelper, который содержит методы для взаимодействия
    # с элементами на странице логина.
    LoginPage = LoginPageHelper(browser)
    # 3. Клик по кнопке логина
    LoginPage.click_login()
    #Проверка:Проверяем,что на странице авторизации при пустых полях логина и пароля и после клика
    #на кнопку - Войти в Одноклассники, возникает текс - Введите логин
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

#Тест 2
@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустом поле логина в форме авторизации')
@allure.feature('Тест Login Page')
@allure.story('Негативный:Аутентификация:Не заполняем пароль')
def test_empty_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.push_text('MyLogin')
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR


