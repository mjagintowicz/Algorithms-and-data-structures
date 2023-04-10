# nieskończone


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = None  # nowe pole gdzie będzie wysokość węzła


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
        self.root, diff = self.insert_rec(self.root, key, value)

    def insert_rec(self, node, key, value):
        if node is None:
            node = Node(key, value)
            self.set_height(node)
            diff = self.calc_dif(node)
            return node, diff
        if node.key > key:
            node.left, diff = self.insert_rec(node.left, key, value)
            self.set_height(node)
            diff = self.calc_dif(node)
            if diff == 2 and self.calc_dif(node.right) > 0:
                node = self.ll_rot(node)
            elif diff == 2 and self.calc_dif(node.right) < 0:
                node = self.rl_rot(node)
            elif diff == -2 and self.calc_dif(node.left) > 0:
                node = self.lr_rot(node)
            elif diff == -2 and self.calc_dif(node.left) < 0:
                node = self.rr_rot(node)
            return node, diff
        elif node.key < key:
            node.right, diff = self.insert_rec(node.right, key, value)
            self.set_height(node)
            diff = self.calc_dif(node)
            if diff == 2 and self.calc_dif(node.right) > 0:
                node = self.ll_rot(node)
            elif diff == 2 and self.calc_dif(node.right) < 0:
                node = self.rl_rot(node)
            elif diff == -2 and self.calc_dif(node.left) > 0:
                node = self.lr_rot(node)
            elif diff == -2 and self.calc_dif(node.left) < 0:
                node = self.rr_rot(node)
            return node, diff
        else:
            node.value = value
            diff = self.calc_dif(node)
            return node, diff

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
        self.root, diff = self.delete_rec(self.root, key)

    def delete_rec(self, node, key):
        if node.key > key:
            node.left, diff = self.delete_rec(node.left, key)
            self.set_height(node)
            diff = self.calc_dif(node)
            if diff == 2 and self.calc_dif(node.right) > 0:
                node = self.ll_rot(node)
            elif diff == 2 and self.calc_dif(node.right) < 0:
                node = self.rl_rot(node)
            elif diff == -2 and self.calc_dif(node.left) > 0:
                self.lr_rot(node)
            elif diff == -2 and self.calc_dif(node.left) < 0:
                node = self.rr_rot(node)
            return node, diff
        elif node.key < key:
            node.right, diff = self.delete_rec(node.right, key)
            self.set_height(node)
            diff = self.calc_dif(node)
            if diff == 2 and self.calc_dif(node.right) > 0:
                node = self.ll_rot(node)
            elif diff == 2 and self.calc_dif(node.right) < 0:
                node = self.rl_rot(node)
            elif diff == -2 and self.calc_dif(node.left) > 0:
                node = self.lr_rot(node)
            elif diff == -2 and self.calc_dif(node.left) < 0:
                node = self.rr_rot(node)
            return node, diff
        else:
            if node.left is None and node.right is None:
                self.set_height(node)
                diff = self.calc_dif(node)
                return None, diff
            elif node.left is not None and node.right is None:
                self.set_height(node)
                diff = self.calc_dif(node)
                return node.left, diff
            elif node.left is None and node.right is not None:
                self.set_height(node)
                diff = self.calc_dif(node)
                return node.right, diff
            else:
                min = self.find_min(node.right)
                node.value = min.value
                node.key = min.key
                node.right, diff = self.delete_rec(node.right, min.key)
                self.set_height(node)
                diff = self.calc_dif(node)
                if diff == 2 and self.calc_dif(node.right) > 0:
                    node = self.ll_rot(node)
                elif diff == 2 and self.calc_dif(node.right) < 0:
                    node = self.rl_rot(node)
                elif diff == -2 and self.calc_dif(node.left) > 0:
                    node = self.lr_rot(node)
                elif diff == -2 and self.calc_dif(node.left) < 0:
                    node = self.rr_rot(node)
                return node, diff

    def find_min(self, node):
        if node.left is None:
            return node
        node = self.find_min(node.left)
        return node

    def tree_height(self):
        return self.height_rec(self.root)

    def set_height(self, node):
        node.height = self.height_rec(node)

    def get_height(self, node):
        return node.height

    def height_rec(self, node):
        if node is None:
            return 0
        left = self.height_rec(node.left)
        right = self.height_rec(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1

    def ll_rot(self, node):
        old_node = Node(node.key, node.value)
        old_node.right = None
        old_node.left = node.left
        self.get_height(old_node)
        node = node.right
        if node.left is None:
            node.left = old_node
            self.set_height(node)
            return node
        else:
            left_child = node.left
            node.left = old_node
            self.set_height(node)
            node = self.insert_help(node, left_child.key, left_child.value, left_child.left, left_child.right)
            return node

    def rr_rot(self, node):
        old_node = Node(node.key, node.value)
        old_node.left = None
        old_node.right = node.right
        self.get_height(old_node)
        node = node.left
        if node.right is None:
            node.right = old_node
            self.set_height(node)
            return node
        else:
            right_child = node.right
            node.right = old_node
            self.set_height(node)
            node = self.insert_help(node, right_child.key, right_child.value, right_child.left, right_child.right)
            return node

    def insert_help(self, node, key, value, left, right):
        if node is None:
            node = Node(key, value)
            node.left = left
            node.right = right
            return node
        if node.key > key:
            node.left = self.insert_help(node.left, key, value, left, right)
            return node
        elif node.key < key:
            node.right = self.insert_help(node.right, key, value, left, right)
            return node

    def lr_rot(self, node):
        left_child = node.left
        node.left = node.left.right
        left_child.right = None
        if node.left.left is None:
            node.left.left = left_child
        else:
            lost_child = node.left.left
            node.left.left = left_child
            node = self.insert_help(node, lost_child.key, lost_child.value, lost_child.left, lost_child.right)
        node = self.rr_rot(node)
        return node

    def rl_rot(self, node):
        right_child = node.right
        node.right = node.right.left
        right_child.left = None
        if node.right.right is None:
            node.right.right = right_child
        else:
            lost_child = node.right.right
            node.right.right = right_child
            node = self.insert_help(node, lost_child.key, lost_child.value, lost_child.left, lost_child.right)
        node = self.ll_rot(node)
        return node

    def calc_dif(self, node):
        l_ = self.height_rec(node.left)
        r_ = self.height_rec(node.right)
        return r_ - l_


def main():
    tree = Root()
    tree.insert(50, 'A')
    tree.insert(15, 'B')
    tree.insert(62, 'C')
    tree.insert(5, 'D')
    tree.insert(2, 'E')
    tree.insert(1, 'F')
    tree.insert(11, 'G')
    tree.insert(100, 'H')
    tree.insert(7, 'I')
    tree.insert(6, 'J')
    tree.insert(55, 'K')
    tree.insert(52, 'L')
    tree.insert(51, 'M')
    tree.insert(57, 'N')
    tree.insert(8, 'O')
    tree.insert(9, 'P')
    tree.insert(10, 'R')
    tree.insert(99, 'S')
    tree.insert(12, 'T')
    tree.print_tree()

    tree.print_()

    print(tree.search(10))

    tree.delete__(50)
    tree.delete__(52)
    tree.delete__(11)
    tree.delete__(57)
    tree.delete__(1)
    tree.delete__(12)

    tree.insert(3, 'AA')
    tree.insert(4, 'BB')
    tree.delete__(7)
    tree.delete__(8)
    tree.print_tree()


main()


