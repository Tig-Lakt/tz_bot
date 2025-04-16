"""
Модуль config.constants

Содержит константы и настройки, используемые в проекте, такие как токен бота,
пути к файлам с данными.
"""

import os
import sys
import logging
from utils import get_bot_token, update_config_file

# Обновление файла config.yaml
update_config_file()

# Получение абсолютного пути к корневому каталогу проекта.
# Получение пути к текущему файлу (constants.py),
# затем переходим на один уровень выше, чтобы получить путь к PROJECT_PATH.
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Добавляем путь к проекту в sys.path, чтобы можно было импортировать модули из проекта.
sys.path.insert(0, PROJECT_PATH)

# Получение токен бота из переменной окружения или файла конфигурации..
TOKEN = get_bot_token()


# Пути к файлам с данными.
# os.path.join() обеспечивает кросс-платформенную совместимость.
DATA_DIR = os.path.join(PROJECT_PATH, "data") # Создаем переменную для пути к директории с данными
USER_FILE = os.path.join(DATA_DIR, "user_file.xlsx")
DATABASE_DIR = os.path.join(PROJECT_PATH, "database", 'my_database.db')