#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    alt = ["+", "-", "*", "/"]
    function = [add, sub, mul, div]
    x = int(sys.argv[1])
    y = int(sys.argv[3])
    for i, j in enumerate(alt):
        if sys.argv[2] == j:
            print("{} {} {} = {}".format(x, j, y, function[i](x, y)))
            break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
