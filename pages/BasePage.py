# Родитель-страница для наших страниц
# Здесь опишем, то как мы будем искать элементы на странице +
# метод,которым будут пользоваться предки

# Вызываем класс-задержку для WebDriver.
#Например,кликнули на кнопку и ждем появление всплывающего окна 7 сек
from selenium.webdriver.support.wait import WebDriverWait
# Вызываем класс-описатель: как ждать ?
from selenium.webdriver.support import expected_conditions

class BasePage:
    #Конструктор класс
    def __init__(self, driver):
        #
        self.driver = driver

    #Функция поиска элментов на странице
    def find_element(self, locator, time=5):
        #Мы создаем объект и потом возращаем его,в котором передаем драйвер и время,которое драйверу нужно ждать
        #Дррайвер подожди (until) пока элемент на странице станет видимым
        #Алгоритм работы функции
        #1.Передаем в функцию локатор
        #2.Ждем,что элемент стал видимым - 5 сек
        #3.Возвращаем элемент класса WebElement (Значит доступны метожды работы класса WebElement)
        return WebDriverWait(self.driver).until(expected_conditions.visibility_of_element_located(locator), message=f"Не удалось найти элемент {locator}")

    #Функция перехода по URL
    def get_url(self,url):
        return self.driver.get(url)