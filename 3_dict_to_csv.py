"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

user_inf = [
    {'Name': 'Olga', 'Age': '28', 'Job': 'sales manager'},
    {'Name': 'Roman', 'Age': '30', 'Job': 'psychologist'},
    {'Name': 'Anna', 'Age': '26', 'Job': 'sales director'},
    {'Name': 'Fedor', 'Age': '36', 'Job': 'engineer'},
]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('user_if.csv', 'w', encoding='utf-8') as inf:
        fields = ['Name', 'Age', 'Job']
        writer= csv.DictWriter(inf, fields, delimiter=';')
        writer.writeheader()
        for user in user_inf:
            writer.writerow(user)

if __name__ == "__main__":
    main()
