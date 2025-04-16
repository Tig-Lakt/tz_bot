import sqlite3
from config import DATABASE_DIR


async def create_models():
    """
    Создает таблицу в базе данных, если она еще не существует.

    В случае ошибки при работе с базой данных, выводит сообщение об ошибке.
    """
    
    try:
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect(DATABASE_DIR)
        cursor = connection.cursor()

        # Создание таблицы links
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            xpath TEXT NOT NULL,
            price INTEGER NOT NULL
        )
        ''')
    except Exception as e:
        print(f"Ошибка {e}")
    
    finally:
        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()