from ds.linked_list import Node, print_linkedlist

"""
Q: Reverse a linked list
"""
def reverse(root):
    rev = None
    i = root
    j = root.next

    while j is not None:
        i.next = rev
        rev = i
        i = j
        j = i.next
    i.next = rev
    rev = i
    return rev

def test_reverse():
    a = Node(1, Node(2, Node(3, Node(4, None))))
    b = reverse(a)
    print_linkedlist(b)


"""
Q: Check whether a linked list is a palindrome or not
"""
def check_palindrome(root, root_rev):
    if root is None:
        return root_rev
    rev = check_palindrome(root.next, root_rev)
    if rev and rev.value == root.value:
        if rev.next is None:
            return True
        else:
            return rev.next
    else:
        return None

def is_palindrome(root):
    return check_palindrome(root, root)

def test_is_palindrome():
    a = Node(1, Node(2, Node(3, Node(2, Node(1, None)))))
    print_linkedlist(a)
    print(is_palindrome(a))
    a = Node(1, Node(2, Node(2, Node(1, None))))
    print_linkedlist(a)
    print(is_palindrome(a))
    a = Node(1, Node(2, Node(3, Node(3, Node(1, None)))))
    print_linkedlist(a)
    print(is_palindrome(a))

test_is_palindrome()