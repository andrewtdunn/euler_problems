import sys

def get_factors(input_num):
    factors = []
    for i in range(1, input_num/2 + 1):
        if input_num % i == 0:
            factors.append(i)
    return factors

def get_sum_of_divisors(input_num):
    return sum(get_factors(input_num))

def count_pairs(input_hash):
    pairs = 0
    for val in input_hash.values():
        print(val)
        if val > 1:
            pairs += (val * (val-1)) / 2
    return pairs

def get_amicable_numbers(input_hash):
    amicable_numbers = []
    for val_array in input_hash.values():
        if (len(val_array) > 1):
            for val in val_array:
                amicable_numbers.append(val)
    return amicable_numbers

def main():
    input_num = int(sys.argv[1])
    amicable_numbers = set({})
    for i in range(1, input_num):
        sum_of_divisors = get_sum_of_divisors(i)
        if (sum_of_divisors == i):
            continue
        if get_sum_of_divisors(sum_of_divisors) == i:
            amicable_numbers.add(sum_of_divisors)
    
    # amicable_numbers = get_amicable_numbers(sums_of_divisors_hash)

    print(amicable_numbers)
    # print(sum(amicable_numbers))

    print(sum(amicable_numbers))



if (__name__) == '__main__':
    main()