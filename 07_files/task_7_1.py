# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
# Открываем файл ospf.txt в режиме чтения
with open("ospf.txt", "r") as file:
    for line in file:
        # Убираем лишние пробелы и разбиваем строку по пробелам
        parts = line.strip().split()
        # Извлекаем нужные элементы, основываясь на структуре строки
        prefix = parts[1]                          # Префикс (например, 10.0.24.0/24)
        ad_metric = parts[2].strip("[]")           # AD/Metric, убираем квадратные скобки
        next_hop = parts[4].strip(",")             # Next-Hop, убираем запятую
        last_update = parts[5].strip(",")          # Last update, убираем запятую
        outbound_interface = parts[6]              # Outbound Interface

        # Форматируем вывод в требуемом виде
        print(f"Prefix                {prefix}")
        print(f"AD/Metric             {ad_metric}")
        print(f"Next-Hop              {next_hop}")
        print(f"Last update           {last_update}")
        print(f"Outbound Interface    {outbound_interface}")
        print()  # Пустая строка для разделения вывода между записями
