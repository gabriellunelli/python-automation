import requests, time, os

sites = [
    'https://google.com',
    'https://github.com',
    'https://site-que-nao-existe-123456789.com',
    'https://youtube.com'
]

while True:
    os.system('cls')

    print('\n========================\n')
    print(' WEBSITE STATUS CHECKER')
    print('\n========================\n')

    for site in sites:

        try:
            
            start = time.time()
            response = requests.get(site, timeout=30)
            hour = time.localtime()
            end = time.time()

            if response.status_code == 200:
                print(f'[{hour.tm_hour}:{hour.tm_min}:{hour.tm_sec}] {site} → ✓ ONLINE | {(end - start) * 1000:.2f} ms')

            else:
                print(f'⚠ HTTP ERROR | {response.status_code}')

        except:
            print(f'{site} → ✗ SEM RESPOSTA')

    print('\n========================\n')
    time.sleep(10)