from datetime import datetime as dt

def add_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as f:
        f.write(f'{time} add {data}\n')

def del_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as f:
        f.write(f'{time} del {data}\n')