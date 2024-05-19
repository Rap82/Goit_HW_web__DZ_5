import asyncio
from concurrent.futures import ThreadPoolExecutor # Exsecutor для потоків 
import requests
from timing import async_timed, sync_timed


urls = [
    "https://goit.global/ua/",
    "https://www.pravda.com.ua/news/2024/05/13/7455502/",
    "https://api.privatbank.ua/#p24/exchangeArchive",
    "https://www.youtube.com"
    ]

def get_preview (url : str) -> tuple[str, str]:
    result = requests.get(url)
    return url, result.text[:25] # Повертаємо url сайту і перших 25 символів з його сторінки *[:25] - зріз з 0 по 25 символ з стрічки.

@sync_timed("Початок роботи синхроної функції") # Власний декоратор для заміру часу виконання синхроної функції
def main_sync():
    """ синхрона функція яка за вказаних  *url з сторінки бере зріз із перших 25 символів добавлає їх в список і вкінці виводить в вигляді кортежу (url,[:25])"""
    results = []
    for url in urls :
        results.append(get_preview (url))
    return results

@async_timed("Початок роботи Асинхроної функції") # Власний декоратор для заміру часу виконання асинхроної функції
async def main():
    """ асинхрона функція яка за вказаних  *url з сторінки бере зріз із перших 25 символів добавлає їх в список і вкінці виводить в вигляді кортежу (url,[:25])"""
    results = []
    loop = asyncio.get_running_loop() # Запускаєм асинхроний event loop
    with ThreadPoolExecutor(10) as pool : # За допомогою менеджера контексут запускаємо асинхроне виконанн синхроної функції *get_preview  в 10 потоків
        futures =  [loop.run_in_executor(pool, get_preview , url ) for url in  urls]
        async_result = await asyncio.gather(*futures)
    return async_result

  
if __name__ == "__main__" :

    print(f"Час затрачений синхроною функцією {main_sync()}") # Принтемо результити виконання синхроної функції

    print(f"Час затрачений асинхроною функцією {asyncio.run(main())}") # принтимо результати виконання асинхроної функції




