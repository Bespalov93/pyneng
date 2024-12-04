# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
import re

def generate_description_from_cdp(file_name):
    result = {}  # Словарь для хранения интерфейсов и их описаний
    # Регулярное выражение для извлечения данных из строки
    regex = r"^([A-Za-z0-9]+)\s+(Eth\s\d+/\d+)\s+(\d+)\s+([A-Za-z\s]+)\s+(\d+)\s+(Eth\s\d+/\d+)$"
   
    # Открываем файл с выводом show cdp neighbors
    with open(file_name, "r") as file:
        for line in file:
            # Ищем строку, которая соответствует нужному формату
            match = re.match(regex, line)
            if match:
                remote_device = match.group(1)  # Локальный интерфейс (например, Eth 0/0)
                local_port = match.group(2)  # Удаленное устройство (например, SW1)
                remote_port = match.group(6)  # Удаленный порт (например, Eth 0/1)
                
                # Формируем описание для интерфейса
                description = f"description Connected to {remote_device} port {remote_port}"
                
                # Добавляем описание в словарь
                result[local_port] = description

    return result
