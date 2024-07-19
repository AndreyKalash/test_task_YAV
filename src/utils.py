import datetime


def time_until_next_update() -> int:
    """
    Вычисляет количество секунд до следующего обновления курсов валют.

    Следующее обновление запланировано на 00:05 следующего дня.
    Добавляется 1 секунда для гарантии перехода на следующий день.

    :return: Количество секунд до следующего обновления
    """
    # Получаем текущее время
    now: datetime.datetime = datetime.datetime.now()

    # Вычисляем время следующего обновления (00:05 следующего дня)
    tomorrow: datetime.datetime = now.replace(
        hour=0, minute=5, second=0, microsecond=0
    ) + datetime.timedelta(days=1)

    # Вычисляем разницу во времени и переводим в секунды
    seconds_until_update: int = int((tomorrow - now).total_seconds())

    return seconds_until_update 