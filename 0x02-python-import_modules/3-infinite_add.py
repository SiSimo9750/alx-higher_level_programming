#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for j in range(1, len(argv)):
        total = total +int(argv[j])
    print(total)
