# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLANы, например:
        {"FastEthernet0/1": [10, 20], "FastEthernet0/2": [11, 30]}
    trunk_template - список команд для порта в режиме trunk

    Возвращает список всех портов в режиме trunk с конфигурацией на основе шаблона
    """
    slovar={}

    for intf, vlans in intf_vlan_mapping.items():
        result = []  # Список для хранения итоговой конфигурации
        # Добавляем строку с интерфейсом
        
        for command in trunk_template:
            if "allowed vlan" in command:
                # Если команда "switchport trunk allowed vlan", добавляем конкретные VLANы
                vlan_list = ",".join(str(vlan) for vlan in vlans)  # Преобразуем список VLAN в строку
                result.append(f"{command} {vlan_list}")
            else:
                # Остальные команды добавляем без изменений
                result.append(command)
            slovar[intf]=result
    return slovar
