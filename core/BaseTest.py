# Родительский тест для всех НАШИХ тестов
import pytest
from selenium import webdriver

#Функция отвечает за открытие и закрытие браузера
#scope(период) со значением session (при каждом запуске тестов pytest генерит сессию. Тоесть период работы фикстуры - сессия)
@pytest.fixture(scope='session')
def browser():
    # Будем тестировать в браузере Chrome
    options = webdriver.ChromeOptions()
    # Задаем для браузера русскую локаль
    options.add_argument("--lang=ru")
    # Для запуска в Selenium Grid
    driver = webdriver.Remote(command_executor="http://5.181.109.28:4444",options=options)
    #Будем тестировать в браузере Chrome
    #driver = webdriver.Chrome()
    #Добавляем для фикстуры паузу. Пауза снимется когда закончится сессия.Тоесть тест выполнится и пауза снимется и браузер закроется (Чтобы окно не висело)
    yield driver
    if driver:
        driver.quit()