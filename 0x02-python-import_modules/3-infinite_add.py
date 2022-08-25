#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv)
    sum_args = 0
    for i in range(1, num_args):
        sum_args += int(argv[i])
    print("{:d}".format(sum_args))
