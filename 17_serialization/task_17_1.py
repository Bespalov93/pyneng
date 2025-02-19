# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import re
import csv

def write_dhcp_snooping_to_csv(filenames, output):
    # Регулярное выражение и заголовок
    regux = r'^([0-9A-Fa-f:]+)\s+(\d{1,3}(?:\.\d{1,3}){3})\s+(\d+)\s+(\S+)\s+(\d+)\s+(\S+)$'
    header = ["switch", "mac", "ip", "vlan", "interface"]

    # Открываем выходной CSV-файл один раз
    with open(output, mode="w", newline="") as output_file:
        writer = csv.writer(output_file)
        # Записываем заголовок
        writer.writerow(header)

        # Обрабатываем каждый файл из списка filenames
        for filename in filenames:
            # Имя коммутатора из имени файла
            com_name = filename.split('_')[0]
            
            # Открываем файл для чтения данных
            with open(filename, "r") as file:
                for line in file:
                    match = re.match(regux, line)
                    if match:
                        # Извлекаем данные из регулярного выражения
                        mac = match.group(1)
                        ip = match.group(2)
                        vlan = match.group(5)
                        interface = match.group(6)
                        # Формируем строку данных и записываем её
                        row = [com_name, mac, ip, vlan, interface]
                        writer.writerow(row)  # Добавляем строку в CSV

