# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re
def get_ints_without_description(file_name):
    current_interface = None  # Переменная для хранения текущего интерфейса
    result = []  # Список для хранения интерфейсов без описания
    regex_interface = r"^\s*interface\s+(\S+)"  # Регулярное выражение для поиска интерфейса
    regex_description = r"^\s*description\s+"  # Регулярное выражение для поиска строки с description
    has_description = False  # Флаг, указывающий на наличие description для текущего интерфейса

    with open(file_name, "r") as file:
        for line in file:
            match_interface = re.search(regex_interface, line)  # Проверка на интерфейс
            match_description = re.search(regex_description, line)  # Проверка на описание

            if match_interface:
                # Если был найден интерфейс и у этого интерфейса не было description,
                # добавляем его в список
                if current_interface and not has_description:
                    result.append(current_interface)
                
                current_interface = match_interface.group(1)  # Обновляем текущий интерфейс
                has_description = False  # Сбрасываем флаг наличия description для нового интерфейса

            elif match_description:
                # Если нашли строку с description, ставим флаг, что интерфейс имеет описание
                has_description = True

        # После обработки всех строк, если у последнего интерфейса нет description, добавляем его
        if current_interface and not has_description:
            result.append(current_interface)

    return result
