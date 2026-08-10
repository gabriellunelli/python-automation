import psutil
import time
import os

while True:
    os.system('cls')
    
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('C:\\')
    processes = psutil.process_iter()
    num_process = 0
    for process in processes:
        num_process += 1

    print(f'CPU: {cpu}%')
    print(f'RAM: {ram.percent}%')
    print(f'DISK: {disk.percent}%')
    print(f'PROCESSES: {num_process}')
    print('=========================')
