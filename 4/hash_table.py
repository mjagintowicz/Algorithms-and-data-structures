#nieskonczone
import random


class Elem:

    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:

    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2

    def gen_hash_code(self, key):
        if isinstance(key, str):
            new_key = 0
            for letter in key:
                new_key += ord(letter)
            new_key %= self.size
            return new_key
        elif isinstance(key, int):
            new_key = key
            new_key %= self.size
            return new_key
        else:
            return None

    def resolve_collision(self, key):
        i = 0
        n_key = key
        while self.tab[n_key] is not None:
            if self.tab[n_key].key is None or self.tab[n_key].data is None:
                break
            n_key = (self.gen_hash_code(key) + self.c1*i + self.c2*i**2) % self.size
            i += 1
        return n_key

#jakies dziwne to
    def resolve_collision_quadratic(self, key):
        perm = list(range(0, self.size))
        perm = random.sample(perm, len(perm))
        for elem in perm:
            if elem == 0:
                inx = perm.index(elem)
                break
        perm[inx] = perm[0]
        perm[0] = 0

        i = 0
        n_key = key
        while self.tab[n_key] is not None:
            if self.tab[n_key].key is None or self.tab[n_key].data is None:
                break
            n_key = (self.gen_hash_code(key) + self.c1 * i + self.c2 * i ** 2) % self.size
            i += 1
            if self.tab[n_key] is not None:
                if self.tab[n_key].key is not None or self.tab[n_key].data is not None:
                    for it in range(1, len(perm)):
                        n_key = (perm[it] + n_key) % self.size
                        if self.tab[n_key] is not None:
                            if self.tab[n_key].key is not None or self.tab[n_key].data is not None:
                                break
                        else:
                            break
        return n_key

    def search(self, key):
        hash_code = self.gen_hash_code(key)
        if self.tab:
            for elem in self.tab:
                if self.gen_hash_code(elem.key) is not None and self.gen_hash_code(elem.key) == hash_code and elem.key == key:
                    return elem.data
        try:
            raise ValueError('Brak danej')
        except ValueError as err:
            print(err)

    def is_full(self):
        count = 0
        for elem in self.tab:
            if elem is not None:
                if elem.key is not None and elem.data is not None:
                    count += 1
        if count == self.size:
            return True
        else:
            return False

    def insert(self, key, data):
        new_item = Elem(key, data)
        new_key = self.gen_hash_code(key)
        if not self.tab[new_key] and not self.is_full(): #jeśli nie ma takiego klucza, to dodaj nowy
            self.tab[new_key] = new_item
        elif self.is_full():
            added = False
            for elem in self.tab:
                if self.gen_hash_code(elem.key) == new_key and elem.key == key:
                    elem.data = data
                    added = True
                    break
            if added is False:
                try:
                    raise ValueError('Brak miejsca')
                except ValueError as err:
                    print(err)
        else:
            if self.c2 == 0:
                new_key = self.resolve_collision(new_key)
            else:
                new_key = self.resolve_collision_quadratic(new_key)
            self.tab[new_key] = new_item

    def remove(self, key):
        removed = False
        new_key = self.gen_hash_code(key)
        for elem in self.tab:
            if self.gen_hash_code(elem.key) == new_key and elem.key == key:
                elem.key = None
                elem.data = None
                elem = None
                removed = True
                break
        if removed is False:
            try:
                raise ValueError('Brak danej')
            except ValueError as err:
                print(err)

    def __str__(self):
        s = '{'
        it = 0
        for elem in self.tab:
            it += 1
            if elem is not None and elem.key is not None and elem.data is not None:
                s += '{}'.format(elem.key)
                s += ': '
                s += '{}'.format(elem.data)
            else:
                s += 'None'
            if it != self.size:
                s += ', '
            else:
                s += '}'
        return s


def fun1(size, c1=1, c2=0):
    tab = HashTable(size, c1, c2)
    asc = 65
    for it in range(16):
        if it == 7:
            tab.insert(18, chr(asc))
        elif it == 8:
            tab.insert(31, chr(asc))
        else:
            tab.insert(it, chr(asc))
        asc += 1

    print(tab)

    print(tab.search(5))
    print(tab.search(14))

    tab.insert(5, 'Z')
    print(tab.search(5))

    tab.remove(5)
    print(tab)

    print(tab.search(31))

    tab.remove(31)
    print(tab)

    tab.insert('test', 'W')
    print(tab)


def fun2(size, c1=1, c2=0):
    tab = HashTable(size, c1, c2)
    asc = 65
    for it in range(13, 26):
        if it == 19:
            tab.insert(18, chr(asc))
        elif it == 20:
            tab.insert(31, chr(asc))
        else:
            tab.insert(it, chr(asc))
        asc += 1

    print(tab)


def main():
    fun1(13)
    fun2(13)
    fun2(13, 0, 1)
    fun1(13, 0, 1)


main()
