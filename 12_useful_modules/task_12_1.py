# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess


def ping_ip_addresses(ip_addresses):
    reachable = []
    unreachable = []
    
    for ip in ip_addresses:
        # Команда для пинга
        command = ['ping', '-c', '3', ip]  # Для Linux/Mac. Для Windows нужно использовать 'ping', '-n', '3', ip
        
        try:
            # Выполняем команду
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Если команда выполнилась успешно (выходной код 0), значит IP доступен
            if result.returncode == 0:
                reachable.append(ip)
            else:
                unreachable.append(ip)
        except Exception as e:
            # В случае ошибки при выполнении пинга (например, не найден путь или ошибка сети)
            unreachable.append(ip)
    
    return (reachable, unreachable)
