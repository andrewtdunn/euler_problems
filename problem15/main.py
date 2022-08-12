import sys
print("ok")

num_steps = 0


import math

def pe15(n):
    n_fact = math.factorial(n)
    return math.factorial(2 * n) / n_fact / n_fact


def main(num):
    print(num)
    print(pe15(int(num)))
    


if (__name__) == "__main__":
    main(sys.argv[1])

