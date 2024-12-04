# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re

def get_ip_from_cfg(filename):
    # Словарь для хранения интерфейсов и их IP-адресов с масками
    interfaces = {}

    # Регулярные выражения для поиска имени интерфейса и IP-адреса с маской
    interface_pattern = re.compile(r"interface (\S+)")
    ip_pattern = re.compile(r"ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)")

    # Открываем файл и обрабатываем его построчно
    with open(filename, 'r') as f:
        current_interface = None
        for line in f:
            # Ищем строку с именем интерфейса
            interface_match = interface_pattern.search(line)
            if interface_match:
                current_interface = interface_match.group(1)

            # Ищем строку с IP-адресом и маской на текущем интерфейсе
            ip_match = ip_pattern.search(line)
            if ip_match and current_interface:
                ip_address = ip_match.group(1)
                subnet_mask = ip_match.group(2)
                # Добавляем интерфейс и его настройки в словарь
                interfaces[current_interface] = (ip_address, subnet_mask)

    return interfaces
