import sys
from decimal import Decimal

def get_substring_length(text):
    first_char = text[0]
    repeat_length = 0
    for i, char in enumerate(text):
        if i > 0 and char == first_char:
            repeat_length = i + 1
            if text[1:repeat_length] == text[repeat_length: 2 * repeat_length - 1]:
                break
    return repeat_length
    

def main():
    max_repeat = 0
    max_repeat_num = None

    for i in range(2, int(sys.argv[1])):
        decimal_pattern = Decimal(1)/Decimal(i)
        decimal_pattern = str(decimal_pattern)[2:]
        # print("[%s]: %s" % (i, decimal_pattern))
        substring_length = get_substring_length(decimal_pattern)
        if (substring_length > max_repeat):
            max_repeat = substring_length
            max_repeat_num = i

    print("max repeat: %s" % max_repeat_num)

if (__name__) == "__main__":
    main()