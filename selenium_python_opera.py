# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as OperaService
from webdriver_manager.opera import OperaDriverManager

options = webdriver.ChromeOptions()

options.binary_location = "C:\\Program Files\\Opera GX\\opera.exe"
options.add_argument("--no-sandbox")
options.add_argument("--no-first-run")
options.add_experimental_option('w3c', True)
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options, service=OperaService(OperaDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
