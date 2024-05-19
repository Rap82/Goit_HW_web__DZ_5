from datetime import datetime, timedelta
import argparse


from aiofile import async_open
import aiohttp
import asyncio

from prettytable import PrettyTable



URL_PRIVAT = "https://api.privatbank.ua/p24api/exchange_rates"


async def exchange_rate(currencies, date):
    async with aiohttp.ClientSession() as session:
        date = date.strftime("%d.%m.%Y")
        url = f"{URL_PRIVAT}?json&date={date}"
        headers = {"Accept": "application/json"}

        async with session.get(url, headers=headers) as response:
            try:
                data = await response.json()
                if "exchangeRate" in data:
                    rates = data["exchangeRate"]
                    d = {}
                    date_rates = {date: d}
                    for rate in rates:
                        if rate["currency"] in currencies:
                            d.update(
                                {
                                    rate["currency"]: {
                                        "sale": rate["saleRate"],
                                        "purchase": rate["purchaseRateNB"],
                                    }
                                }
                            )
                    return date_rates
            except aiohttp.ClientError as e:
                print(f"Error {e}, when occcurind data")
                return None


async def exchange_rates(currencies, days):
    tasks = []
    start_day = datetime.now()
    for i in range(days):
        date = start_day - timedelta(days=i)
        tasks.append(exchange_rate(currencies, date))

    return await asyncio.gather(*tasks)


async def main(currencies, num_of_days):

    currencies_str = ", ".join(currencies)

    if num_of_days > 10:
        print("Курс валюти для переглду небільше 10 днів.")
        return {}

    exchange_ratess = await exchange_rates(currencies, num_of_days)

    async with async_open("log.txt", mode="w") as log_file:
        await log_file.write(f"Currencise: {currencies_str}.\nExchange date: {datetime.now()}\n")

    return exchange_ratess


def build_table(data):

    table = PrettyTable(["Дата", "Валюта", "Купівля", "Продаж"])
    table.align = "l"

    flattened_result = [(date, rates) for item in data for date, rates in item.items()]
    flattened_result.sort(key=lambda x: datetime.strptime(x[0], "%d.%m.%Y"))

    for date, rates in flattened_result:
        row_added = False
        for currency, rate in rates.items():
            purchase = rate["purchase"]
            sale = rate["sale"]
            if not row_added:
                table.add_row([date, currency, f"{purchase:.2f}", f"{sale:.2f}"])
                row_added = True
            else:
                table.add_row(["", currency, f"{purchase:.2f}", f"{sale:.2f}"])

    return table


if __name__ == "__main__":
    
    print("Доступні валюти: USD, EUR, GBP, PLZ ")
    
    currencies = input("Ведіть валюту  ").upper()
    
    num_of_days = int(input("Введіть кількість днів "))
    
    result = asyncio.run(main(currencies, num_of_days))
    print(build_table(result))