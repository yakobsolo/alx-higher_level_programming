#!/usr/bin/python3
import sys
num_arguments = len(sys.argv[1:])
sum = 0
i = 1
while num_arguments >= i:
    sum = sum + int(sys.argv[i])
    i += 1
print(sum)
