#!/user/bin/python

# Work out the first ten digits of the sum of the 
# following one-hundred 50 digit numbers

import sys

def read_file(input_file):
    print("reading %s" % input_file)
    file = open(input_file, 'r')
    lines = file.readlines()
    carry = 0
    curr_digits = []
    for i in range(49, -1, -1):
        running_sum = carry
        for line in lines:
            print(line)
            curr_digit = line[i]
            print("digit %s" % curr_digit)
            running_sum = running_sum + int(curr_digit)
            # running_sum = running_sum+int(curr_digit)
            print("running_sum: %s" % running_sum)
            print("ones case %s" % (running_sum % 10))
        ones_case = running_sum % 10
        print(running_sum)
        new_carry = running_sum / 10
        carry = new_carry
        if (i <= 10):
            curr_digits.insert(0, ones_case)
    print(curr_digits)
    print(carry)
    print(len(str(carry)))
    carry_digits = [int(a) for a in str(carry)]
    print("- - - - - - ")
    if (carry_digits[0] > 0):
        print("carry digits")
        print(carry_digits, len(carry_digits))
        to_add = 10 - len(carry_digits)
        print(to_add)
        for j in range(0, to_add):
            carry_digits.append(curr_digits[j])
        print(carry_digits, len(carry_digits))
        print(sum(carry_digits))
    else: 
        print(curr_digits)
        print(sum(curr_digits))





def main():
    print("main")
    file = sys.argv[1]
    print(file)
    input = read_file(file)

if __name__ == "__main__":
    main()
    