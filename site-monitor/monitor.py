import requests
import os

sites_string = os.getenv("MONITOR_SITES", "https://google.com") # Приравниваю к response получение статуса сайта

sites = sites_string.split(",")

for site in sites:
    try:
        response = requests.get(site)

        if response.status_code == 200: # .status_code возвращает цифровой код от сервера в виде числа
            print (f"[OK] {site} available")
        else:
            print (f"[ERROR] {site} вернул код {response.status_code}")

    except requests.exceptions.RequestException as Error:
        print(f"[CRITICAL] Не удалось подключиться к {site}. Ошибка {Error}")
