# nieskończone


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Root:

    def __init__(self):
        self.root = None

    def search(self, key):
        return self.search_rec(self.root, key)

    def search_rec(self, node, key):
        if node.key == key:
            return node.value
        if node.key > key:
            value = self.search_rec(node.left, key)
            return value
        elif node.key < key:
            value = self.search_rec(node.right, key)
            return value
        else:
            return None

    def insert(self, key, value):
        self.root = self.insert_rec(self.root, key, value)

    def insert_rec(self, node, key, value):
        if node is None:
            node = Node(key, value)
            return node
        if node.key > key:
            node.left = self.insert_rec(node.left, key, value)
            return node
        elif node.key < key:
            node.right = self.insert_rec(node.right, key, value)
            return node
        else:
            node.value = value
            return node

    def print_(self):
        s = ''
        lst = self.print_rec_lst(self.root, [])
        for node in lst:
            s += '{}'.format(node[0])
            s += ' '
            s += '{}'.format(node[1])
            if node == lst[len(lst)-1]:
                break
            else:
                s += ','
        print(s)

    def print_rec_lst(self, node, lst=[]):
        if node.left is None:
            lst.append((node.key, node.value))
            if node.right is not None:
                lst = self.print_rec_lst(node.right, lst)
            return lst
        lst = self.print_rec_lst(node.left, lst)
        lst.append((node.key, node.value))
        if node.right is not None:
            lst = self.print_rec_lst(node.right, lst)
            return lst
        return lst

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)
            print()
            print(lvl * " ", node.key, node.value)
            self.__print_tree(node.left, lvl + 5)

    def delete__(self, key):
        self.root = self.delete_rec(self.root, key)

    def delete_rec(self, node, key):
        if node.key > key:
            node.left = self.delete_rec(node.left, key)
            return node
        elif node.key < key:
            node.right = self.delete_rec(node.right, key)
            return node
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is not None and node.right is None:
                return node.left
            elif node.left is None and node.right is not None:
                return node.right
            else:
                min = self.find_min(node.right)
                node.value = min.value
                node.key = min.key
                node.right = self.delete_rec(node.right, min.key)
            return node

    def find_min(self, node):
        if node.left is None:
            return node
        node = self.find_min(node.left)
        if node.right is not None:
            node = self.find_min(node.right)
            return node
        return node

    def height(self):
        return self.height_rec(self.root)

    def height_rec(self, node):
        if node is None:
            return 0
        left = self.height_rec(node.left)
        right = self.height_rec(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1


def main():
    tree = Root()

    tree.insert(50, 'A')
    tree.insert(15, 'B')
    tree.insert(62, 'C')
    tree.insert(5, 'D')
    tree.insert(20, 'E')
    tree.insert(58, 'F')
    tree.insert(91, 'G')
    tree.insert(3, 'H')
    tree.insert(8, 'I')
    tree.insert(37, 'J')
    tree.insert(60, 'K')
    tree.insert(24, 'L')

    tree.print_tree()
    tree.print_()

    print(tree.search(24))

    tree.insert(20, 'AA')
    tree.insert(6, 'M')
    tree.delete__(62)
    tree.insert(59, 'N')
    tree.insert(100, 'P')
    tree.delete__(8)
    tree.delete__(15)
    tree.insert(55, 'R')
    tree.delete__(50)
    tree.delete__(5)
    tree.delete__(24)

    print(tree.height())

    tree.print_tree()
    tree.print_()


main()
