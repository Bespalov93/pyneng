# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import re
import yaml

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

# Пример использования
output = '''
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
'''

# Вызов функции
parsed_result = parse_sh_cdp_neighbors(output)

# Печать результата
print(parsed_result)



def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    # Итоговый словарь для топологии
    topology = {}

    # Обрабатываем каждый файл
    for filename in list_of_files:
        with open(filename, 'r') as file:
            output = file.read()
            # Парсим данные из вывода
            parsed_topology = parse_sh_cdp_neighbors(output)
            
            # Обновляем общий словарь с топологией
            for device, interfaces in parsed_topology.items():
                if device not in topology:
                    topology[device] = {}
                
                for local_int, connections in interfaces.items():
                    if local_int not in topology[device]:
                        topology[device][local_int] = {}
                    for neighbor_device, neighbor_port in connections.items():
                        # Обрабатываем информацию о соединениях
                        if neighbor_device not in topology[device][local_int]:
                            topology[device][local_int][neighbor_device] = neighbor_port

                        # Для соседнего устройства тоже добавляем связь
                        if neighbor_device not in topology:
                            topology[neighbor_device] = {}
                        if neighbor_port not in topology[neighbor_device]:
                            topology[neighbor_device][neighbor_port] = {}
                        topology[neighbor_device][neighbor_port][device] = local_int

    # Если задан параметр для сохранения в файл, записываем топологию в YAML
    if save_to_filename:
        with open(save_to_filename, 'w') as yaml_file:
            yaml.dump(topology, yaml_file, default_flow_style=False)

    return topology
