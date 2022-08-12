import sys

def distinct_powers(a, b):
    print("distinct powers: %s, %s" % (a, b))
    powers = set({})
    for i in range(a, b+1):
        for j in range(a, b+1):
            powers.add(pow(i, j))
    return powers

def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    dp = distinct_powers(a, b)
    print(len(dp))

if (__name__) == "__main__":
    main()