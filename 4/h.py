#nieskonczone

class Elem:

    def __init__(self, key, data):
        self.key = key
        self.data = data


class Hash:

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
            try:
                raise ValueError('Wrong data type!')
            except ValueError as err:
                print(err)

    def collision(self, inx):
        return (self.tab[inx] + self.c1*inx + self.c2*inx**2) % self.size

    def search(self, key):
        hash_code = self.gen_hash_code(key)
        if self.tab:
            for elem in self.tab:
                if self.gen_hash_code(elem.key) == hash_code:
                    if elem.data == self.tab[hash_code].data:
                        return self.tab[hash_code].data
        else:
            return None

    def insert(self, key, data):
        new_item = Elem(key, data)
        new_key = self.gen_hash_code(key)
        if not self.tab[new_key] and new_key < self.size: #jeśli nie ma takiego klucza, to dodaj nowy
            self.tab[new_key] = new_item
        elif new_key >= self.size:
            return None
        # 2 przypadki - nadpisać albo dodać nowy
        else:
            added = False
            for elem in self.tab:
                if self.gen_hash_code(elem.key) == new_key:
                    if elem.key == key:
                        elem.data == data
                        added = True
                        break
            if added is False:
                while self.tab[new_key] is not None:
                    new_key = self.collision(new_key)
                self.tab[new_key] = new_item

    def remove(self, key):
        removed = False
        for elem in self.tab:
            if elem.key == key:
                elem.data = None
                removed = True
                break
        if not removed:
            print("Brak danej")

    def __str__(self):
        s = '{'
        it = 0
        for elem in self.tab:
            it += 1
            if elem is not None:
                s += '{}'.format(elem.key)
                s += ': '
                s += '{}'.format(elem.data)
            else:
                s += 'None'
            if it != self.size:
                s += ', '
            else:
                s+= '}'
        return s


def f1(size, c1=1, c2=0):
    tab = Hash(size, c1, c2)
    tab.insert(1, 'A')
    print(tab)


f1(13)

