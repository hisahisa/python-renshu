import inspect

def sample_code():
    # 上の図と同じ木を作る。
    binary_search_tree = BinarySearchTree()
    for value in (8, 3, 1, 6, 10, 4, 7, 14, 13, 12):
        binary_search_tree.insert(value)
    print(binary_search_tree.root.left.list())
    print(binary_search_tree.list())
    # [1, 3, 4, 6, 7, 8, 10, 13, 14]
    g = binary_search_tree.generator()
    print(list(g))
    # [1, 3, 4, 6, 7, 8, 10, 13, 14]

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = BinarySearchNode(value)

    def list(self):
        if self.root:
            return self.root.list()
        else:
            return []

    def generator(self):
        if self.root:
            return self.root.generator()
        else:
            # empty generator
            return (_ for _ in range(0))

class BinarySearchNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchNode(value)


    #
    # 1. 再帰呼び出しでリストを生成する関数を
    #
    def list(self):
        sorted_list = []
        if self.left:
            sorted_list.extend(self.left.list())
        sorted_list.append(self.value)
        if self.right:
            sorted_list.extend(self.right.list())
        return sorted_list

    #
    # 2. ジェネレータで書き換え
    #    再起の部分には yeild ではなく yiled from を使う。
    #
    def generator(self):
        if self.left:
            print("l:  {}".format(self.left.value))
            yield from self.left.generator()

        print("s: {}".format( self.value))
        yield self.value

        if self.right:
            print("r:  {}".format(self.right.value))
            yield from self.right.generator()


if __name__ == '__main__':
    sample_code()

