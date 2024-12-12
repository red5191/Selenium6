# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)

from selenium import webdriver # импортируем webdriver
from selenium.webdriver.chrome.service import Service as ChromeService # Импортируем службу Service отвечающую за запуск chromedriver под именем "ChromeService"
from webdriver_manager.chrome import ChromeDriverManager # Импортируем службу которая пытается загрузить последний драйвер для Chrome

options = webdriver.ChromeOptions() # Присваиваем переменной options значение актуальных параметров из пакета webdriver библиотеки selenium через объект класса Options
options.add_experimental_option("detach",True) # Без понятия что делает эта строка, но без неё браузер сразу же закрывается
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install())) # Создаем объект driver класса webdriver.Chrome с ранее заданными параметрами
base_url = 'https://www.saucedemo.com/' # Задаем переменной base_url в качестве значения строку содержащую желаемую ссылку
driver.get(base_url) # Даем драйверу команду открыть переменную как ссылку
driver.maximize_window() # Даём драйверу команду растянуть окно браузера на весь экран