#!/user/bin/python

# Work out the first ten digits of the sum of the 
# following one-hundred 50 digit numbers

import sys

def read_file(input_file):
    file = open(input_file, 'r')
    lines = file.readlines()
    total = 0
    for line in lines:
        total += int(line)
    first_ten = str(total)[0:10]
    print(first_ten)




def main():
    print("main")
    file = sys.argv[1]
    print(file)
    read_file(file)

if __name__ == "__main__":
    main()
    