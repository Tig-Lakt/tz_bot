import os
import sys

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Добавление пути к проекту в sys.path, для возможности импорта модулей.
sys.path.insert(0, PROJECT_PATH)

import pandas as pd
from config import USER_FILE


async def read_file():
    """
        Чтение пользовательского файла.

        Returns:
            Структуру данных Pandas - DataFrame.
        """
    data = pd.read_excel(USER_FILE)
    return data