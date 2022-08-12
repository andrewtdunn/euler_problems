import sys


def main(num):
    chain_length_champ = 0
    start_champ = num
    for i in range(int(num), 0, -1):
        start = int(i)
        values = [i]
        while values[len(values) - 1] != 1:
            curr_val = values[len(values) - 1]
            if (curr_val % 2) == 0:
                values.append(curr_val/2)
            else: 
                values.append((3 * curr_val) + 1)
            # print(values, len(values))
        if len(values) > chain_length_champ:
            chain_length_champ = len(values)
            start_champ = i
    print(start_champ)

if __name__ == '__main__':
    main(sys.argv[1])