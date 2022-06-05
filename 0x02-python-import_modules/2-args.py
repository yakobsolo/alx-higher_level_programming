#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("{} argument.".format(0))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        num_len = len(sys.argv[1:])
        i = 1
        while num_len >= i:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
