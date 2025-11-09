#!/usr/local/bin/python3
from bfi import interpret

def bf_eval(code: str) -> str:
    return interpret(code, input_data='', buffer_output=True)

def py_eval(code: str) -> str:
    return str(eval(code))

code = input('> ')

if any(c not in '<>-+.,[]' for c in code):
    print('bf only pls')
    exit()

a = None
b = None

try:
    a = bf_eval(code)
    print("bf:", a)
except Exception as e:
    print("bf error:", e)

try:
    b = py_eval(code)
    print("py:", b)
except Exception as e:
    print("py error:", e)

if a == b:
    print(open('flag.txt', 'r').read())
