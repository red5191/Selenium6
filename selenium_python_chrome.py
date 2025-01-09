# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)

# импортируем необходимые библиотеки и элементы
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# создаем и настраиваем экземпляр driver класса webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# создаем переменную содержащую базовую ссылку и открываем её с помощью созданного ранее driver
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# вводим логин
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys('standard_user')
print('Введен логин')

# вводим пароль
password = driver.find_element(By.NAME , "password")
password.send_keys('secret_sauce')
print("Введен пароль")

# нажимаем кнопку авторизации
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()
print("Произведен \"клик\" по кнопке")

# создаем переменные для текущей и контрольной ссылки
get_url = driver.current_url
print(f'Текущий URL: {get_url}')
control_url = 'https://www.saucedemo.com/inventory.html'

# удостоверяемся что при авторизации открывается верный URL
assert control_url == get_url
print('URL корректен')

# с помощью локатора создаем переменную содержащую текст уникального для контрольного URL элемента
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_products = text_products.text
print(value_text_products)

# удостоверяемся что уникальный для URL элемент доступен при выполнении теста
assert value_text_products == 'Products'
print('Заголовок корректен')
