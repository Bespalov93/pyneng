# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re

def parse_sh_cdp_neighbors(output):
    # Разделение вывода на строки
    lines = output.splitlines()

    # Регулярное выражение для строки с данными о соседях
    pattern = r"(\S+)\s+(\S+\s+\S+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+\S+\s+(\S+\s+\S+)"
    
    # Результат, который будем заполнять
    result = {}
    
    device_name = None  # Чтобы запомнить имя устройства

    for line in lines:
        line = line.strip()  # Убираем пробелы в начале и в конце строки
        
        # Проверка на начало команды (например, R4>show cdp neighbors)
        if '>' in line and 'show cdp neighbors' in line:
            device_name = line.split('>')[0]  # Извлекаем имя устройства перед символом '>'
        
        # Пропускаем строки, которые не содержат данных о соседях
        if not device_name or line.startswith('Device ID'):
            continue
        
        # Проверка строк с данными о соседях
        match = re.match(pattern, line)
        if match and device_name:
            device_id = match.group(1)  # Device ID
            local_int = match.group(2)  # Local Interface
            port_id = match.group(7)  # Port ID

            # Форматируем интерфейсы с пробелами
            local_int = local_int.replace(' ', ' ')  # Пробел для интерфейса
            port_id = port_id.replace(' ', ' ')  # Пробел для порта

            # Сохраняем данные в словарь
            if device_name not in result:
                result[device_name] = {}

            # Добавляем соединение в результат
            result[device_name][local_int] = {device_id: port_id}
    
    return result
