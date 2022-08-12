import sys

def sum_diagonals(dimension_size):
    print("finding corner sum of square of size %s." % dimension_size)
    curr_corners = [1]
    side_length = 0
    while curr_corners[-1] < (dimension_size * dimension_size):
        side_length += 2
        for i in range(1, 5):
            new_corner = curr_corners[-1] + side_length
            curr_corners.append(new_corner)
    print(sum(curr_corners))

            




def main():
    sum_diagonals(int(sys.argv[1]))

if (__name__) == '__main__':
    main()