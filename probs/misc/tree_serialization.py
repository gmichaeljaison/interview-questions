import ds.tree as tree


def serialize(root):
    pre = [node.data for node in tree.pre_order(root)]
    inord = [node.data for node in tree.in_order(root)]

    return [pre, inord]


def deserialize(pre, inord):
    if len(pre) == 0:
        return None

    root = tree.BNode(pre[0])
    root_i = inord.index(root.data)
    left_tree_cnt = len(inord[:root_i])
    root.left = deserialize(pre[1:left_tree_cnt+1], inord[:root_i])
    root.right = deserialize(pre[left_tree_cnt+1:], inord[root_i+1:])
    return root


if __name__ == '__main__':

    n3 = tree.BNode(3)
    n4 = tree.BNode(4)
    n2 = tree.BNode(2, n3, n4)

    n7 = tree.BNode(7)
    n6 = tree.BNode(6, left=n7)
    n5 = tree.BNode(5, right=n6)

    root = tree.BNode(1, n2, n5)

    tree_data = serialize(root)
    print(tree_data[0])
    print(tree_data[1])

    de_root = deserialize(tree_data[0], tree_data[1])

    [print(node.data) for node in tree.pre_order(root)]
