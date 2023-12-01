#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    else:
        print("{:d} argument".format(len(argv) - 1), end="")
        if len(argv) > 2:
            print("s", end="")
        print(":")
        for j in range(1, len(argv)):
            print("{:d}: {:s}".format(j, argv[j]))
