import threading

def print_number():
    for i in range(5):
        print(f'Number : {i}')

def print_char():
    for i in 'ABCDEF':
        print(f'Char : {i}')


target1=threading.Thread(target=print_char)
target2=threading.Thread(target=print_number)

target1.start()

target2.start()
target1.join()
target2.join()