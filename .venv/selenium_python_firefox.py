# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)

from selenium import webdriver # импортируем webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService # Импортируем службу Service отвечающую за запуск firefoxdriver под именем "FirefoxService"
from webdriver_manager.firefox import GeckoDriverManager # Импортируем службу которая пытается загрузить последний драйвер для Firefox

options = webdriver.FirefoxOptions() # Присваиваем переменной options значение актуальных параметров из пакета webdriver библиотеки selenium через объект класса Options
driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install())) # Создаем объект driver класса webdriver.Firefox с ранее заданными параметрами
base_url = 'https://www.saucedemo.com/' # Задаем переменной base_url в качестве значения строку содержащую желаемую ссылку
driver.get(base_url) # Даем драйверу команду открыть переменную как ссылку
driver.maximize_window() # Даём драйверу команду растянуть окно браузера на весь экран