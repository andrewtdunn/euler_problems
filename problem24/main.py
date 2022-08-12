print("ok")

from operator import index
import sys
from itertools import permutations 

        
def get_next(input_list):
    # print("input: %s" % input_list)
    # iterate from the back
    for i in range(len(input_list) - 1, 0, -1):
        # print("input_list[i]: %s" % input_list[i])
        # print("input_list[i-1]: %s" % input_list[i-1])
        if input_list[i] > input_list[i-1]:
            index_to_be_replaced = i-1
            # print("inversion at %s" % index_to_be_replaced)
            next = None
            haystack = input_list[index_to_be_replaced + 1:]
            needle = input_list[index_to_be_replaced] + 1
            if needle in haystack:
                next = input_list[index_to_be_replaced] + 1
            else: 
                next = max(haystack)
            # print("next: %s" % next)
            next_index = input_list.index(next)

            temp = input_list[index_to_be_replaced]
            input_list[index_to_be_replaced] = input_list[next_index]
            input_list[next_index] = temp
            start = input_list[:index_to_be_replaced + 1]
            end = input_list[index_to_be_replaced + 1:]
            end.sort()
            # print("start: %s" % start)
            # print("end: %s" % end)
            input_list = start + end
            #print(input_list[i-1:])
            break
    return input_list


def main():
    start = sys.argv[1].split(',')
    start = [int(a) for a in start]
    target = start[::-1]
    iteration_target = int(sys.argv[2])


    # p = permutations(start) 
    # #print(len(list(p)))
    # p_list = list(p)
    # print(list(p))


    current = start
    i = 0
    while (current != target and i < iteration_target):
        print("%s current: %s" % (i,current))
        current = get_next(current)
        i+= 1

    formatted_current = ('').join([str(a) for a in current])
    print("current: %s" % formatted_current)
    print("iterations: %s" % i)


if (__name__) == "__main__":
    main()

