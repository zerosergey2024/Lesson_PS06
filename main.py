import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = 'https://www.divan.ru/category/stoly-i-stulya'

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)

# Находим все карточки с названиями с помощью названия класса
# Названия классов берём с кода сайта
stolies = driver.find_elements(By.CLASS_NAME, 'div.WdR1o')

# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию столов
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for stoly in stolies:
   try:
   # Находим элементы внутри вакансий по значению
   # Находим название сзделия
     name = stoly.find_element(By.CSS_SELECTOR, 'span.name').text
     # Находим ценник
     price = stoly.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text

     # Находим ссылку с помощью атрибута 'href'
     link = stoly.find_element(By.CSS_SELECTOR, 'a.0').get_attribute('href')
   # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   except:
       print("произошла ошибка при парсинге")
       continue

   # Вносим найденную информацию в список
   parsed_data.append([name, price, link])

# Закрываем подключение браузер
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("stol.csv", 'w',newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название стола', 'Цена изделия', 'ссылка на изделие'])

    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)