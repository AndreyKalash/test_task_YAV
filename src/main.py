import asyncio
from currency import fetch_currency_rates
from bot import start_bot
from utils import time_until_next_update


async def main() -> None:
    """
    Основная асинхронная функция приложения.
    
    Инициализирует получение курсов валют, запускает периодическое обновление
    и стартует бота.
    
    :return: None
    """
    # Получаем курсы валют при запуске
    await fetch_currency_rates()

    # Запускаем периодическое обновление курсов
    asyncio.create_task(periodic_update())
    
    # Запускаем бота
    await start_bot()


async def periodic_update() -> None:
    """
    Асинхронная функция для периодического обновления курсов валют.
    
    Выполняется в бесконечном цикле, обновляя курсы в начале каждого нового дня.
    
    :return: None
    """
    while True:
        # Вычисляем время до следующего обновления
        delay = time_until_next_update()
        # Ждем до следующего обновления
        await asyncio.sleep(delay)
        # Обновляем курсы валют
        await fetch_currency_rates()


if __name__ == "__main__":
    # Запускаем основную асинхронную функцию
    asyncio.run(main())
