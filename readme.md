### 📋 Тестовое задание для Python Junior Developer

#### 📚 Описание задания
Необходимо разработать приложение (чат-бот) для отображения актуального курса валют.

#### 🛠️ Функциональные требования

1. **Сервис получения курсов валют**:
    - Ежедневно получает XML файл с курсами валют с сайта Центрального банка России (ЦБ РФ) по [этой ссылке](https://cbr.ru/scripts/XML_daily.asp).
    - Обновляет данные в Redis, для каждого курса валюты свой ключ.

2. **Сервис бота**:
    - Отвечает на команду `/exchange`, например: `/exchange USD RUB 10` и отображает стоимость 10 долларов в рублях.
    - Отвечает на команду `/rates`, отправляя пользователю актуальные курсы валют.

#### 🚀 Дополнительные рекомендации

- [x] Для получения XML файла с курсами рекомендуется использовать `aiohttp`.
- [x] Для работы с XML рекомендуется использовать `xml.etree.ElementTree`.
- [x] Для работы с Redis рекомендуется использовать `redis`.
- [x] Для создания бота рекомендуется использовать `aiogram`.
- [x] Для запуска приложения использовать `docker-compose`.
