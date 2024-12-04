# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений
  и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
   в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена
  информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы (именно в этом порядке):
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается
на sh_vers. Вы можете раскомментировать строку print(sh_version_files),
чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob

sh_version_files = glob.glob("sh_vers*")
# print(sh_version_files)

headers = ["hostname", "ios", "image", "uptime"]


import re
import csv

def parse_sh_version(output):
    # Регулярное выражение для iOS, image, uptime
    ios_regex = r"Version (\S+)"
    image_regex = r"System image file is \"(\S+)\""
    uptime_regex = r"uptime is (.+)"
    
    ios = re.search(ios_regex, output)
    image = re.search(image_regex, output)
    uptime = re.search(uptime_regex, output)
    
    # Извлекаем данные, если есть совпадения
    ios_version = ios.group(1)[:len(ios.group(1))-1] if ios else None
    image_file = image.group(1) if image else None
    uptime_duration = uptime.group(1) if uptime else None
    
    return ios_version, image_file, uptime_duration

def write_inventory_to_csv(data_filenames, csv_filename):
    headers = ["hostname", "ios", "image", "uptime"]

    with open(csv_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Записываем заголовок
        writer.writerow(headers)
        
        # Обрабатываем каждый файл в списке
        for filename in data_filenames:
            # Извлекаем имя хоста из имени файла
            hostname = filename.split('_')[2].split('.')[0]
            
            # Читаем содержимое файла
            with open(filename, "r") as file:
                output = file.read()
            
            # Получаем данные из вывода команды с помощью parse_sh_version
            ios, image, uptime = parse_sh_version(output)
            
            # Создаем строку для CSV с данными о коммутаторе
            row = [hostname, ios, image, uptime]
            writer.writerow(row)

