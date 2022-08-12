import sys

def get_factors(num):
    factors = []
    for i in range(1, num/2 + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def get_abundant_numbers(limit):
    abundant_numbers = []
    for i in range(1, limit):
        factors = get_factors(i)
        if sum(factors) > i:
            abundant_numbers.append(i)
    return abundant_numbers

def test_for_abundant_sum(limit, abundant_numbers):
    # make list of possible sums less than limit
    positives = set({})
    for i in abundant_numbers:
        for j in abundant_numbers:
            total = i + j
            if total < limit:
                positives.add(total)
    print("there are %s numbers that can be expressed as the sum of two abundant numbers under %s." % (len(positives), limit))
    unmatched = []
    for x in range(1, limit):
       if not x in positives:
           unmatched.append(x)
    return sum(unmatched)



def main():
    limit = int(sys.argv[1])
    abundant_numbers = get_abundant_numbers(limit)
    abundant_sum = test_for_abundant_sum(limit, abundant_numbers)
    print(abundant_sum)

if (__name__) == '__main__':
    main()