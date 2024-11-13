from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import allure

BASE_URL = "https://ok.ru/"
EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"

#Тест 1
@allure.feature('Test Login Page')
@allure.story('Negative:Autentifikaciya:Ne zapolnyaem login i parol')
def test_empty_login_and_password(browser):
    #1.Инициализация страницы: Вызывается конструктор класса-родителя BasePage, который, вероятно,
    # содержит общие методы для работы со страницами. В этом случае вызывается метод get_url(BASE_URL),
    # который открывает указанный URL (в данном случае, базовый URL для страницы авторизации).
    with allure.step('1.Otkryvaem brauzer s ukazannym URL'):
        BasePage(browser).get_url(BASE_URL)
        #2. Создается экземпляр класса LoginPageHelper, который содержит методы для взаимодействия
        # с элементами на странице логина.
    with allure.step('2.Nachinaem rabotu so stranicej autentifikacii'):
        LoginPage = LoginPageHelper(browser)
    # 3. Клик по кнопке логина
    with allure.step('3.Nazhimaem na knopku "Vojti v Odnoklassniki"'):
        LoginPage.click_login()
    with allure.step('5.Proverka, chto na stranice avtorizacii pri pustyh polyah logina i parolya i posle klika na knopku - Vojti v Odnoklassniki, voznikaet teks - Vvedite login'):
        #Проверка:Проверяем,что на странице авторизации при пустых полях логина и пароля и после клика
        #на кнопку - Войти в Одноклассники, возникает текс - Введите логин
        assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR

#Тест 2
@allure.feature('Test Login Page')
@allure.story('Negative:Autentifikaciya:Ne zapolnyaem parol')
def test_empty_password(browser):
    with allure.step('1.Otkryvaem brauzer s ukazannym URL'):
        BasePage(browser).get_url(BASE_URL)
    with allure.step('2.Nachinaem rabotu so stranicej autentifikacii'):
        LoginPage = LoginPageHelper(browser)
    with allure.step('3.Zapolnyaem pole logina'):
        LoginPage.push_text('MyLogin')
    with allure.step('4.Nazhimaem na knopku "Vojti v Odnoklassniki"'):
        LoginPage.click_login()
    with allure.step('5.Proverka, chto na stranice avtorizacii pri pustom pole parolya i posle klika na knopku - Vojti v Odnoklassniki, voznikaet tekst - Vvedite parol'):
        assert LoginPage.get_error_text() == EMPTY_PASSWORD_ERROR

#Temp
@allure.feature('Test Login Page')
@allure.story('Negative:Autentifikaciya:Ne zapolnyaem login and parol')
def test_empty_password(browser):
    with allure.step('1.Otkryvaem brauzer s ukazannym URL'):
        BasePage(browser).get_url(BASE_URL)
    with allure.step('2.Nachinaem rabotu so stranicej autentifikacii'):
        LoginPage = LoginPageHelper(browser)
    with allure.step('3.Nazhimaem na knopku "Vojti v Odnoklassniki"'):
        LoginPage.click_button()