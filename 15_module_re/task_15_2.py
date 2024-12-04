# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re

def parse_sh_ip_int_br(filename):
    result = []
    
    # Регулярное выражение для извлечения данных из строки, включая "administratively down"
    regex = re.compile(r'(\S+)\s+(\S+|\S+)\s+\S+\s+\S+\s+(administratively down|up|down)\s+(up|down)')
    
    with open(filename) as f:
        for line in f:
            match = regex.search(line)
            if match:
                # Извлекаем данные и добавляем их в список
                interface = match.group(1)
                ip_address = match.group(2)
                status = match.group(3)
                protocol = match.group(4)
                result.append((interface, ip_address, status, protocol))
    
    return result
