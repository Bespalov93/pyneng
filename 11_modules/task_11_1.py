# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Функция обрабатывает вывод команды show cdp neighbors и возвращает словарь соединений между устройствами.
    """
    connections = {}
    lines = command_output.strip().splitlines()

    # Извлечение имени устройства из первой строки (до символа '>')
    device_name = lines[0].split('>')[0]

    # Пропускаем строки заголовка, находим первую строку с данными о соединении
    start_index = 0
    for index, line in enumerate(lines):
        if line.strip().startswith("Device ID"):
            start_index = index + 1  # Стартуем со следующей строки после "Device ID"
            break

    # Обрабатываем только строки с данными о соединениях
    for line in lines[start_index:]:
        # Проверяем, если строка может быть строкой соединения
        if line and len(line.split()) >= 5:  # проверка на минимальное количество элементов
            columns = line.split()
            
            # Удаленное устройство
            remote_device = columns[0]
            
            # Локальный интерфейс
            local_interface = columns[1] + columns[2]  # объединяем, убирая пробел
            
            # Удаленный интерфейс
            remote_interface = columns[-2] + columns[-1]  # объединяем, убирая пробел
            
            # Добавляем соединение в словарь
            connections[(device_name, local_interface)] = (remote_device, remote_interface)
    
    return connections

if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
