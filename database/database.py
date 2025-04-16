
"""
Модуль database.py

Обеспечивает взаимодействие с базой данных sqlite
с использованием библиотеки sqlite3.
"""

import sqlite3
from config import DATABASE_DIR


async def insert_data(title, url, xpath, price):
    """
    Создает таблицу в базе данных, если она еще не существует.

    В случае ошибки при работе с базой данных, выводит сообщение об ошибке.
    """

    try:
        # Соединение с базой данных
        connection = sqlite3.connect(DATABASE_DIR)
        cursor = connection.cursor()

        # Заполнение таблицы links
        cursor.execute(f'''
                       INSERT INTO links (title, url, xpath, price) 
                       VALUES ('{title}', '{url}', '{xpath}', '{price}');
        ''')
    except Exception as e:
        print(f"Ошибка {e}")
    
    finally:
        # Сохранение изменений и закрытие соединений
        connection.commit()
        connection.close()


async def get_sites():
    try:
        # Соединение с базой данных
        connection = sqlite3.connect(DATABASE_DIR)
        cursor = connection.cursor()

        cursor.execute('SELECT DISTINCT url FROM links;')
        sites = cursor.fetchall()
        return sites
    except Exception as e:
        print(f"Ошибка {e}")

    finally:
        # Закрытие соединения
        connection.close()


async def get_prices(url):
    try:
        # Соединение с базой данных
        connection = sqlite3.connect(DATABASE_DIR)
        cursor = connection.cursor()

        cursor.execute("SELECT price FROM links WHERE url = ?", (url,))
        prices = cursor.fetchall()
        return prices
    except Exception as e:
        print(f"Ошибка {e}")

    finally:
        # Закрытие соединения
        connection.close()


async def del_data():
    print('del_data')
    try:
        # Соединение с базой данных
        connection = sqlite3.connect(DATABASE_DIR)
        cursor = connection.cursor()

        cursor.execute("DELETE FROM links;")
        prices = cursor.fetchall()
        return prices
    except Exception as e:
        print(f"Ошибка {e}")

    finally:
        # Сохранение изменений и закрытие соединений
        connection.commit()
        connection.close()