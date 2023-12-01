#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import div, mul, add, sub
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    x1 = int(argv[1])
    op = argv[2]
    x2 = int(argv[3])
    res = 0

    if op == "+":
        res = add(x1, x2)
        print("{} + {} = {}".format(x1, x2, res))
    elif op == "-":
        res = sub(x1, x2)
        print("{} - {} = {}".format(x1, x2, res))
    elif op == "/":
        res = div(x1, x2)
        print("{} / {} = {}".format(x1, x2, res))
    elif op == "*":
        res = mul(x1, x2)
        print("{} * {} = {}".format(x1, x2, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
