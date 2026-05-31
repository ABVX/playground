from prometheus_client import start_http_server, Counter
import requests
import os
import time

REQUEST_COUNTER = Counter("site_checks_total", "Общее количество проверок сайтов")

sites_string = os.getenv("MONITOR_SITES", "https://google.com") # Приравниваю к response получение статуса сайта

sites = sites_string.split(",")

start_http_server(8000)

while True:
    print("Запуск круга проверки сайтов")


    for site in sites:
        try:
            response = requests.get(site)
            REQUEST_COUNTER.inc()

            if response.status_code == 200: # .status_code возвращает цифровой код от сервера в виде числа
                print (f"[OK] {site} available")
            else:
                print (f"[ERROR] {site} вернул код {response.status_code}")

        except requests.exceptions.RequestException as Error:
            print(f"[CRITICAL] Не удалось подключиться к {site}. Ошибка {Error}")

    print("Ожидание 10 секунд до следующей проверки...\n")
    time.sleep(10)
