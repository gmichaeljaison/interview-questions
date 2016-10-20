import ds.graph as graph


Node = graph.Node


class BNode(graph.Node):
    def __init__(self, data, left=None, right=None):
        super().__init__(data)
        self.data = data
        self.children = [left, right]
        self._left = left
        self._right = right

    @property
    def left(self):
        return self.children[0]

    @property
    def right(self):
        return self.children[1]

    @left.setter
    def left(self, left):
        self.children[0] = left

    @right.setter
    def right(self, right):
        self.children[1] = right


def pre_order(root):
    if root is None:
        return

    yield root
    for child in root.children:
        for node in pre_order(child):
            yield node


def in_order(root):
    if root is None:
        return

    # assuming binary tree
    for node in in_order(root.left):
        yield node

    yield root

    for node in in_order(root.right):
        yield node


def post_order(root):
    if root is None:
        return

    for child in root.children:
        for node in post_order(child):
            yield node
    yield root


def height(root):
    pass