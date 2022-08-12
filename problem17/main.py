import sys


class Node:
    def __init__(self, value):
        self.value = int(value)
        self.left = None
        self.right = None

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right

    def __str__(self):
        return "value: %s" % self.value

node_list = []


def read_value_list(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    levels = []
    for line in lines:
        line = line.rstrip()
        num_list = line.split(" ")
        levels.append(num_list)
    return levels

def make_tree(node, depth, width, val_lines):
    if depth < len(val_lines) - 1:
        node.add_left(make_tree(Node(val_lines[depth+1][width]), depth+1, width, val_lines))
        node.add_right(make_tree(Node(val_lines[depth+1][width+1]), depth+1, width+1, val_lines))
    return node
    
max_total = 0

def walk_tree(node, total):
    global max_total
    total += node.value
    if total > max_total:
        max_total = total
    if (node.left):
        walk_tree(node.left, total)
    if (node.right):
        walk_tree(node.right, total)

def main(filename):
    val_lines = read_value_list(filename)
    root = Node(val_lines[0][0])
    global max_total
    make_tree(root, 0,0, val_lines)
    walk_tree(root, 0)
    print("max_total: %s" % max_total)


if (__name__) == '__main__':
    main(sys.argv[1])