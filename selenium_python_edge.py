# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)

from selenium import webdriver  # импортируем webdriver
from selenium.webdriver.edge.service import Service as EdgeService  # Импортируем службу Service отвечающую за запуск chromedriver под именем "EdgeService"
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Импортируем службу которая пытается загрузить последний драйвер для Edge

options = webdriver.EdgeOptions()  # Присваиваем переменной options значение актуальных параметров из пакета webdriver библиотеки selenium через объект класса Options
options.add_experimental_option("detach", True)  # Отвязывает запуск браузера от выполнения кода
driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))  # Создаем объект driver класса webdriver.Edge с ранее заданными параметрами
base_url = 'https://www.saucedemo.com/'  # Задаем переменной base_url в качестве значения строку содержащую желаемую ссылку
driver.get(base_url)  # Даем драйверу команду открыть переменную как ссылку
driver.maximize_window()  # Даём драйверу команду растянуть окно браузера на весь экран
