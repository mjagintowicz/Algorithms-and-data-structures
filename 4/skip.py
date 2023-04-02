# skonczone
import random


def random_level(p):
    lvl = 1
    while random.random() < p:
        lvl = lvl + 1
    return lvl


class Elem:

    def __init__(self, key, data, p=0.5):
        self.key = key
        self.value = data
        self.height = random_level(p)
        self.tab = [None for it in range(self.height)]


class SkipList:

    def __init__(self, height):
        self.head = Elem(None, None)
        self.head.height = height
        self.head.tab = [None for it in range(height)]

    def search(self, key):
        elem = self.head
        for level in reversed(range(self.head.height)):
            while elem.tab[level] is not None and elem.tab[level].key <= key:
                if elem.tab[level].key < key:
                    elem = elem.tab[level]
                elif elem.tab[level].key > key:
                    break
                else:
                    return elem.tab[level].value
        return None

    def insert(self, key, data):
        elem = self.head
        p = []
        inserted = False
        for level in reversed(range(self.head.height)):
            if elem.tab[level] is None:
                p.append(elem)
                continue
            while elem.tab[level] is not None:
                if elem.tab[level].key < key:
                    elem = elem.tab[level]
                    if elem.tab[level] is None:
                        p.append(elem)
                        break
                elif elem.tab[level].key > key:
                    p.append(elem)
                    break
                else:
                    elem.tab[level].value = data
                    inserted = True
                    break
            if inserted:
                break
        if not inserted:
            new_elem = Elem(key, data)
            if new_elem.height > self.head.height:
                new_elem.height = self.head.height
            for lvl in range(new_elem.height):
                prev = p.pop()
                new_elem.tab[lvl] = prev.tab[lvl]
                prev.tab[lvl] = new_elem

    def display_list_(self):
        node = self.head.tab[0]
        keys = []
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        maxlevel = self.head.height
        for lvl in range(maxlevel - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.tab[lvl]
            print("")

    def remove(self, key):
        elem = self.head
        p = []
        for level in reversed(range(self.head.height)):
            found = False
            while elem.tab[level] is not None and elem.tab[level].key <= key:
                if elem.tab[level].key < key:
                    elem = elem.tab[level]
                elif elem.tab[level].key > key:
                    break
                else:
                    found = True
                    p.append(elem)
                    break
        if found:
            found_elem = elem.tab[0]
            for lvl in range(found_elem.height):
                prev = p.pop()
                prev.tab[lvl] = found_elem.tab[lvl]
        else:
            return None

    def __str__(self):
        elem = self.head
        s = ''
        while elem.tab[0] is not None:
            s += '('
            s += '{}'.format(elem.tab[0].key)
            s += ':'
            s += '{}'.format(elem.tab[0].value)
            s += ')'
            elem = elem.tab[0]
            if elem.tab[0] is not None:
                s += ', '
        return s


def main():
    skip = SkipList(random_level(0.5))

    for it in range(1, 16):
        skip.insert(it, chr(it+64))

    print(skip)

    print(skip.search(2))

    skip.insert(2, 'Z')

    print(skip.search(2))

    skip.remove(5)
    skip.remove(6)
    skip.remove(7)

    print(skip)

    skip.insert(6, 'W')

    print(skip)

    reverse_skip = SkipList(random_level(0.5))

    for it in reversed(range(1, 16)):
        reverse_skip.insert(it, chr(it + 64))
    print(reverse_skip)

    print(reverse_skip.search(2))

    reverse_skip.insert(2, 'Z')

    print(reverse_skip.search(2))

    reverse_skip.remove(5)
    reverse_skip.remove(6)
    reverse_skip.remove(7)

    print(reverse_skip)

    reverse_skip.insert(6, 'W')

    print(reverse_skip)


main()
