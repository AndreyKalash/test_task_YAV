from typing import Dict, Optional
import aiohttp
import xml.etree.ElementTree as ET
import redis
from config import REDIS_HOST, REDIS_PORT, CBR_URL

# Инициализация клиента Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


async def fetch_currency_rates() -> None:
    """
    Получает актуальные курсы валют с сайта ЦБ РФ и сохраняет их в Redis.

    :return: None
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(CBR_URL, timeout=10) as response:
                xml_data = await response.text()

        root = ET.fromstring(xml_data)

        with redis_client.pipeline() as pipe:
            for valute in root.findall("Valute"):
                code = valute.find("CharCode").text
                value = valute.find("Value").text.replace(",", ".")
                nominal = valute.find("Nominal").text
                # Расчет курса с учетом номинала
                value = float(value) / float(nominal)

                pipe.set(f"currency:{code}", value)
            pipe.execute()
    except Exception as e:
        print(f"Ошибка при получении курсов валют: {e}")


def get_currency_rate(currency_code: str) -> Optional[float]:
    """
    Получает курс валюты по её коду.

    :param currency_code: Код валюты (например, 'USD', 'EUR')
    :return: Курс валюты или None, если курс не найден
    """
    if currency_code == "RUB":
        return 1.0
    rate = redis_client.get(f"currency:{currency_code}")
    return float(rate) if rate else None


def get_all_rates() -> Dict[str, float]:
    """
    Получает словарь всех доступных курсов валют.

    :return: Словарь вида {код_валюты: курс}
    """
    keys = redis_client.keys("currency:*")
    return {key.split(":")[1]: redis_client.get(key) for key in keys}
