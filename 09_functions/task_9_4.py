# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status=True
    return ignore_status

def convert_config_to_dict(config_filename):
    config_dict = {}
    current_command = None  # Текущая команда верхнего уровня

    with open(config_filename) as file:
        for line in file:
            if line=='\n':
                continue
            else:
		# Игнорируем строки, которые начинаются с "!" или содержат слова из ignore
            	if line.startswith("!") or ignore_command(line, ignore):
                	continue

            # Если строка — команда верхнего уровня (не содержит отступов)
            	if not line.startswith(" "):
                	current_command = line.strip()  # Запоминаем текущую команду верхнего уровня
                	config_dict[current_command] = []  # Создаем запись в словаре для этой команды
            	elif current_command:
                	# Добавляем подкоманду в список значений для текущей команды верхнего уровня
                	config_dict[current_command].append(line.strip())

    return config_dict
