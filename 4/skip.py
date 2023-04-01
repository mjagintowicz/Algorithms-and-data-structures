# nieskonczone
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
                if elem.tab[level].key < key:  # jeśli tak to przejdź na następny element
                    elem = elem.tab[level]
                elif elem.tab[level].key > key:  # jeśli tak jest to dodaj ten node do listy i idź level niżej
                    break  # czyli wyjdź z while
                else:  # kiedy są równe, to po prostu podmień
                    return elem.tab[level].value
        return None

    # insert działa, jak mam dopisywać elementy na sam koniec w miarę
    # nadpisywanie chyba też
    def insert(self, key, data):
        elem = self.head
        p = []
        inserted = False
        for level in reversed(range(self.head.height)):
            if elem == self.head and elem.tab[level] is None:
                p.append(elem)
            while elem.tab[level] is not None:
                if elem.tab[level].key < key:  # jeśli tak to przejdź na następny element
                    elem = elem.tab[level]
                    if elem.tab[level] is None:
                        p.append(elem)
                        break
                elif elem.tab[level].key > key:  # jeśli tak jest to dodaj ten node do listy i idź level niżej
                    p.append(elem)
                    break
                else:  # kiedy są równe, to po prostu podmień
                    elem.tab[level].value = data
                    inserted = True
                    break
            if inserted:
                break
        if not inserted and p:
            new_elem = Elem(key, data)
            if new_elem.height > self.head.height:
                new_elem.height = self.head.height
            it = 0
            clvl = -1
            while p:
                prev = p.pop()
                clvl += 1
                if clvl < it:
                    clvl = it
                for lvl in range(clvl, prev.height):
                    if it >= new_elem.height:
                        break
                    new_elem.tab[lvl] = prev.tab[lvl]  # teraz nowy element wskazuje na to, co jego poprzednik
                    prev.tab[lvl] = new_elem  # a ten poprzednik wskazuje na nowy element
                    it += 1
                if it >= new_elem.height:
                    break

    def display_list_(self):
        node = self.head.tab[0]  # pierwszy element na poziomie 0
        keys = []  # lista kluczy na tym poziomie
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
            return None  # brak klucza

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
    lvl = random_level(0.5)
    skip = SkipList(lvl)
    for it in range(1, 16):
        skip.insert(it, chr(it+64))
    print(skip)
    skip.display_list_()

    print(skip.search(2))

    skip.insert(2, 'Z')
    skip.display_list_()

    print(skip.search(2))

    skip.remove(5)
    skip.display_list_()
    skip.remove(6)
    skip.display_list_()
    skip.remove(7)
    skip.display_list_()

    print(skip)

    skip.insert(6, 'W')
    print(skip)


main()



