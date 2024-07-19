from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from currency import get_currency_rate, get_all_rates
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    """
    Обработчик команды /start.
    
    :param message: Входящее сообщение
    :return: None
    """
    await message.answer(
        "Привет! Я бот для отображения курсов валют. Используй /exchange для конвертации или /rates для просмотра курсов."
    )


@dp.message(Command("exchange"))
async def cmd_exchange(message: types.Message) -> None:
    """
    Обработчик команды /exchange.
    Конвертирует заданное количество одной валюты в другую.
    
    :param message: Входящее сообщение
    :return: None
    """
    args = message.text.split()[1:]
    if len(args) != 3:
        await message.answer("Используйте формат: /exchange USD RUB 10")
        return

    from_currency, to_currency, amount = args
    try:
        amount = float(amount)
    except ValueError:
        await message.answer("Неверный формат суммы")
        return

    from_rate = get_currency_rate(from_currency.upper())
    to_rate = get_currency_rate(to_currency.upper())

    if not all([from_rate, to_rate]):
        await message.answer("Не удалось получить курс для одной из валют")
        return

    # Конвертация валюты
    result = (from_rate / to_rate) * amount

    await message.answer(f"{amount} {from_currency} = {result:.2f} {to_currency}")


@dp.message(Command("rates"))
async def cmd_rates(message: types.Message) -> None:
    """
    Обработчик команды /rates.
    Отправляет пользователю список текущих курсов валют.
    
    :param message: Входящее сообщение
    :return: None
    """
    rates = get_all_rates()
    response = "Текущие курсы валют:\n\n"
    for code, rate in rates.items():
        response += f"{code}: {float(rate):.4f}\n"
    await message.answer(response)


async def start_bot() -> None:
    """
    Запускает бота.
    
    :return: None
    """
    await dp.start_polling(bot)
