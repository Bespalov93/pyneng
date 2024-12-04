# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

# Словарь для выбора шаблона и вопроса по режиму
template_dict = {
    "access": (access_template, "Введите номер VLAN:"),
    "trunk": (trunk_template, "Введите разрешенные VLANы:")
}

# Запрашиваем у пользователя режим и параметры интерфейса
mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")
vlan_info = input(template_dict[mode][1])

# Выбираем шаблон и выводим конфигурацию
selected_template = template_dict[mode][0]
print(f"\ninterface {interface}")
print("\n".join(selected_template).format(vlan_info))
