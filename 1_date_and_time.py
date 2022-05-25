"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    delta_yesterday = timedelta(days=1)
    delta_month_ago = timedelta(days=30)
    date_today = datetime.now()
    date_yesterday = date_today - delta_yesterday
    date_month_ago = date_today - delta_month_ago
    dt = date_today.strftime('%d.%m.%Y')
    dy = date_yesterday.strftime('%d.%m.%Y')
    dma = date_month_ago.strftime('%d.%m.%Y')
    print(f'Вчерашняя дата {dy}')
    print(f'Сегодняшняя дата {dt}')
    print(f'Дата 30 дней назад {dma}')

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(date_string)
    
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/21 12:10:03.234567"))
