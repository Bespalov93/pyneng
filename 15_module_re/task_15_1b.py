# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re

def get_ip_from_cfg(config_filename):
    result = {}
    # Регулярные выражения для поиска интерфейсов и IP-адресов
    intf_regex = re.compile(r'^interface (\S+)')
    ip_regex = re.compile(r' ip address (\S+) (\S+)')
    
    with open(config_filename) as file:
        current_interface = None
        for line in file:
            intf_match = intf_regex.search(line)
            if intf_match:
                # Обновляем текущий интерфейс
                current_interface = intf_match.group(1)
            elif current_interface:
                # Проверяем наличие IP-адреса на текущем интерфейсе
                ip_match = ip_regex.search(line)
                if ip_match:
                    # Если для интерфейса найден IP-адрес, добавляем его в результат
                    if current_interface not in result:
                        result[current_interface] = []
                    # Добавляем кортеж (IP, mask) в список IP-адресов для интерфейса
                    ip_address = ip_match.group(1)
                    mask = ip_match.group(2)
                    result[current_interface].append((ip_address, mask))
    
    # Убираем интерфейсы, для которых нет IP-адресов
    result = {key: value for key, value in result.items() if value}
    
    return result
