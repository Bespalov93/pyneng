# -*- coding: utf-8 -*-
"""
Задание 9.1a

Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли
настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд
   port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_mode_template и шаблона port_security_template,
если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config, с генерацией конфигурации
port-security и без.

Пример вызова функции:
print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    result = []  # Список для хранения итоговой конфигурации

    for intf, vlan in intf_vlan_mapping.items():
        # Добавляем команду интерфейса
        result.append(f"interface {intf}")
        
        # Проходимся по шаблону команд и добавляем их
        for command in access_template:
            if "access vlan" in command:
                # Если команда "switchport access vlan", добавляем конкретный VLAN
                result.append(f"{command} {vlan}")
            else:
                # Остальные команды добавляем без изменений
                result.append(command)

        if psecurity:
            for command in psecurity:
                result.append(command)
    return result
print(generate_access_config(access_config,access_mode_template))
