#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_argv = len(sys.argv)
    if num_argv <= 1:
        print("0 arguments.")
    else:
        if num_argv == 2:
            print("{:d} argument:".format(num_argv - 1))
        else:
            print("{:d} arguments:".format(num_argv - 1))
        for i in range(1, num_argv):
            print("{:d}: {}".format(i, sys.argv[i]))
