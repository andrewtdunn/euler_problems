import sys

def find_sum_of_digit_powers(power):
    print("finding sum of %s powers (max %s)" % (power, pow(10, power) -1))
    min_test = pow(10, power-1)
    max_test = 355000
    positives = []
    for i in range(min_test, max_test):
        digit_string = (str(i))
        # print(digit_string)
        digits_array = [int(a) for a in digit_string]
        # print(digits_array)
        powers = [pow(digit, power) for digit in digits_array]
        if sum(powers) == i:
            positives.append(i)
    print(positives)
    return sum(positives)


def main():
    power = int(sys.argv[1])
    sum = find_sum_of_digit_powers(power)
    print("sum of all the numbers that can be written as the sum of %s powers of their digits: %s" %  (power, sum))

if (__name__) == "__main__":
    main()