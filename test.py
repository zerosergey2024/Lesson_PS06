import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Chrome()

# Указываем сайт
url = 'https://www.divan.ru/category/stoly-i-stulya'

# Открываем веб-страницу
driver.get(url)

# Задаём время ожидания
time.sleep(3)

# Находим все карточки с названиями по классу
stolies = driver.find_elements(By.CLASS_NAME, 'WdR1o')

# Создаём список для хранения данных
parsed_data = []

# Перебираем коллекцию столов
for stoly in stolies:
    try:
        # Находим элементы внутри карточек
        name = stoly.find_element(By.CSS_SELECTOR, 'span').text
        price = stoly.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
        link = stoly.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    # Вносим информацию в список
    parsed_data.append([name, price, link])

# Закрываем браузер
driver.quit()

# Записываем данные в CSV файл
with open("stol.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название стола', 'Цена изделия', 'Ссылка на изделие'])
    writer.writerows(parsed_data)