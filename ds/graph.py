import itertools


class Node:
    # static
    counter = itertools.count(1)

    def __init__(self, data):
        self.id = next(Node.counter)
        self.data = data
        self.children = list()

    def __str__(self):
        return str('Id: {}, data: {}, num_children: {}'.format(self.id, self.data,
                                                               len(self.children)))


class Graph:
    def __init__(self):
        self.nodes = list()

    def add_node(self, node):
        self.nodes.append(node)

    @staticmethod
    def add_edge(node1, node2):
        node1.children.append(node2)
        node2.children.append(node1)

    def add_edge_idx(self, node1_idx, node2_idx):
        Graph.add_edge(self.nodes[node1_idx], self.nodes[node2_idx])
