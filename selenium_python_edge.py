# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.XPATH, "//input[@placeholder = 'Username']")
user_name.send_keys('standard_user')

password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()