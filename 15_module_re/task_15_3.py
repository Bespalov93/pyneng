# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re

def convert_ios_nat_to_asa(input_file, output_file):
    # Открываем файл с правилами Cisco IOS для чтения
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Регулярное выражение для парсинга правил NAT Cisco IOS
    nat_regex = re.compile(
        r'ip nat inside source static tcp (\S+) (\d+) interface (\S+) (\d+)'
    )
    
    # Открываем файл для записи преобразованных правил Cisco ASA
    with open(output_file, 'w') as outfile:
        first_rule = True  # Для контроля пустых строк между правилами
        for line in lines:
            # Ищем соответствие правилу NAT
            match = nat_regex.search(line)
            if match:
                # Извлекаем данные из строки
                inside_ip = match.group(1)
                inside_port = match.group(2)
                interface = match.group(3)
                outside_port = match.group(4)
                
                # Формируем правило для ASA
                # Меняем точку на подчеркивание в имени объекта
                object_name = f"LOCAL_{inside_ip}"
                
                # Записываем объект, перед этим проверяем, нужна ли пустая строка
                if not first_rule:
                    outfile.write("\n")  # Добавляем пустую строку перед следующим правилом
                first_rule = False
                
                # Формируем и записываем правило для ASA
                outfile.write(f"object network {object_name}\n")
                outfile.write(f" host {inside_ip}\n")
                outfile.write(f" nat (inside,outside) static interface service tcp {inside_port} {outside_port}\n")
        
        # Убедимся, что файл заканчивается без лишних пробелов или пустых строк
        outfile.flush()  # Убедимся, что все данные записаны корректно
