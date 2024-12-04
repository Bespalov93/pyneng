# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
filename = 'CAM_table.txt'
cam_table = []
vlan_input=int(input('Введите номер VLAN: '))
with open(filename, "r") as file:
    for line in file:
        # Убираем лишние пробелы по краям и разбиваем строку на части
        parts = line.split()
        
        # Проверяем, что строка содержит нужные данные (всего 4 элемента)
        # 1 элемент - номер VLAN, 2 - MAC-адрес, 4 - интерфейс (3-й игнорируем)
        if len(parts) == 4 and parts[0].isdigit():
            vlan = int(parts[0])
            mac = parts[1]
            interface = parts[3]
            cam_table.append((vlan, mac, interface))
            # Выводим строку в нужном формате

cam_table.sort()

for vlan, mac, interface in cam_table:
    if vlan==vlan_input:
        print(f"{vlan:<8}{mac:<20}{interface}")
