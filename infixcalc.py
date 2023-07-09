#!/usr/bin/env python3
"""Infix calc.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `infixcalc.log`
"""
__version__ = "0.1.0"

import os
import sys

from datetime import datetime

arguments = sys.argv[1:]

#TODO: Exceptions
if not arguments:
    operation = input("Operation: ")
    n1 = input("N1: ")
    n2 = input("N2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Invalid number of arguments")
    print("For example: 'sum 5 5 '")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Invalid Operation")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Create a while repetition + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Invalid Number {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

# TODO: Use dict of functions
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "Anonymous")

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operation}.{n1},{n2} = {result}\n")

# printf(f"{timestamp} - {user} - {operation}.{n1},{n2} = {result}", file=open(filename, "a"))

print(f"The result is {result}")