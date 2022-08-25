#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    P = len(argv)
    print("{:d} {:s}{:s}".format(P - 1, "argument" if P <= 2 else "arguments",
                                 "." if P == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
