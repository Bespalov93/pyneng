# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access_ports = {}
    trunk_ports = {}

    with open(config_filename) as file:
        for line in file:
            line = line.strip()
            # Проверяем, что строка является началом интерфейса
            if line.startswith("interface "):
                interface = line.split()[1]
            # Проверяем, что интерфейс в режиме access и получаем номер VLAN
            elif line=='switchport mode access':
                access_ports[interface] = 1
            elif "switchport mode access" in line:
                access_ports[interface] = None  # Запоминаем интерфейс
            elif "switchport access vlan" in line:
                vlan = int(line.split()[-1])
                access_ports[interface] = vlan  # Обновляем VLAN для access порта
            # Проверяем, что интерфейс в режиме trunk и получаем список VLAN
            elif "switchport trunk allowed vlan" in line:
                vlans = list(map(int, line.split()[-1].split(',')))
                trunk_ports[interface] = vlans

    return access_ports, trunk_ports
