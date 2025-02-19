# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
# Запрашиваем у пользователя ввод
network = input("Введите IP-сеть в формате 10.1.1.0/24: ")

# Разделяем на IP и маску
ip, mask_length = network.split('/')
mask_length = int(mask_length)

# Преобразуем IP в десятичный формат
ip_decimal = ip.split('.')

# Преобразуем IP в двоичный формат
ip_binary = ''.join(format(int(octet), '08b') for octet in ip_decimal)

# Получаем маску в двоичном и десятичном формате
mask_binary = "1" * mask_length + "0" * (32 - mask_length)
mask_decimal = [str(int(mask_binary[i:i+8], 2)) for i in range(0, 32, 8)]

# Формируем вывод
print("Network:")
print(f"{ip_decimal[0]:<10}{ip_decimal[1]:<10}{ip_decimal[2]:<10}{ip_decimal[3]:<10}")
print(f"{ip_binary[0:8]}  {ip_binary[8:16]}  {ip_binary[16:24]}  {ip_binary[24:32]}")

print("\nMask:")
print(f"/{mask_length}")
print(f"{mask_decimal[0]:<10}{mask_decimal[1]:<10}{mask_decimal[2]:<10}{mask_decimal[3]:<10}")
print(f"{mask_binary[0:8]}  {mask_binary[8:16]}  {mask_binary[16:24]}  {mask_binary[24:32]}")
