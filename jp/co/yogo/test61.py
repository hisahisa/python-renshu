class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traverse(node):
    if node is not None:
        for x in traverse(node.left):
            yield x
        yield node.dat
        for x in traverse(node.right):
            yield x


def traverse2(node):
    if node is not None:
        yield from traverse2(node.left)
        yield node.date
        yield from traverse2(node.right)

n = Node
