

class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node


def print_linkedlist(root):
    i = root
    while i is not None:
        print('{}->'.format(i.value), end='')
        i = i.next
