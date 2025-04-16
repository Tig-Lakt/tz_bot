import re
from database.database import (  
    get_sites,
    get_prices,
)


async def get_average_price():
    """
        Получение уникального имени сайта и списка цен.

        Вычисление средней цены зяблика для каждого сайта

        Returns:
            Средняя цена для каждого сайта (int).
        """
    sites = await get_sites()
    sum = 0
    msg = 'Средняя цена зяблика для каждого сайта:\n'
    for site in sites:
        prices = await get_prices(site[0])
        for price in prices:
            sum = sum + price[0]
        
        average_price = round(sum / len(prices), 2)
        msg = msg + site[0] + '--->' + str(average_price) + '\n'
        sum = 0
    return msg