from ds import tree


def find_tree_height():
    n3 = tree.BNode(3)
    n4 = tree.BNode(4)
    n2 = tree.BNode(2, n3, n4)

    n1 = tree.BNode(1, n2, tree.BNode(5))

    print(tree.height(n2))
    print(tree.height(n1))

    n3.left = tree.BNode(6)
    n3.right = tree.BNode(7)
    n3.right.right = tree.BNode(8)

    print(tree.height(n1))


if __name__ == '__main__':
    find_tree_height()
