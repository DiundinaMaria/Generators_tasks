#!/usr/bin/env python3
from decimal import Decimal, MAX_PREC, getcontext
from multiprocessing import Process
from signal import signal, SIGTERM

a = Decimal(3)
b = Decimal(4)
decimal_two = Decimal(2)


# noinspection PyUnusedLocal
def sigterm_handler(signum, frame):
    write_result()


def write_result():
    global a, b, decimal_two
    with open('root_of_11_res.txt', mode='w') as result_file:
        result_file.write(str((a + b) / decimal_two))
        exit(0)


def count_root():
    signal(SIGTERM, sigterm_handler)
    global a, b, decimal_two
    getcontext().prec = MAX_PREC
    while True:
        try:
            middle = (a + b) / decimal_two
            square_of_middle = middle * middle
            if square_of_middle == 11:
                write_result()
            elif square_of_middle < 11:
                a = middle
            else:
                b = middle
        except MemoryError:
            write_result()


proc = Process(target=count_root, name="Root of 11 counter")
proc.start()
proc.join(3600)
if proc.is_alive():
    proc.terminate()
    proc.join()
