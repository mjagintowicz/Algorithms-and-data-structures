# skonczone

tab_size = 6


class Elem:
    def __init__(self):
        self.size = tab_size
        self.tab = [None for i in range(self.size)]
        self.count = 0
        self.next = None

    def insert(self, inx: int, data):
        if inx >= self.count:
            self.tab[inx] = data
        else:
            for it in reversed(range(self.count)):
                if it != inx - 1:
                    self.tab[it+1] = self.tab[it]
            self.tab[inx] = data
        self.count += 1

    def delete1(self, inx: int):
        self.tab[inx] = None
        for it in range(inx, self.count):
            if it != self.count-1:
                self.tab[it] = self.tab[it+1]
            else:
                self.tab[it] = None
        self.count -= 1


class Unrolled:

    def __init__(self):
        self.list = []

    def get(self, inx: int):
        counts = []
        for tab in self.list:
            counts.append(tab.count)
            if sum(counts) > inx:
                for it in range(len(counts)):
                    if inx - counts[it] < 0:
                        return tab.tab[inx]
                    inx -= counts[it]
        try:
            raise ValueError('wrong index!')
        except ValueError as err:
            print(err)

    def insert(self, inx: int, data):
        if not self.list:
            new_tab = Elem()
            self.list.append(new_tab)
            new_tab.insert(0, data)
        else:
            counts = []
            for tab in self.list:
                counts.append(tab.count)
                if inx <= sum(counts):
                    if tab.count != tab_size:
                        for it in range(len(counts)):
                            if inx - counts[it] <= 0:
                                tab.insert(inx, data)
                                break
                            inx -= counts[it]
                        break
                    elif tab.next is None:
                        new_tab = Elem()
                        new_tab.next = tab.next
                        tab.next = new_tab
                        self.list.insert(self.list.index(tab) + 1, new_tab)
                        new_tab.insert(new_tab.count, data)
                        break
                    else:
                        new_tab = Elem()
                        new_tab.next = tab.next
                        tab.next = new_tab
                        self.list.insert(self.list.index(tab)+1, new_tab)
                        tmp_inx = 0
                        for it in range(int(tab_size/2), tab_size):
                            new_tab.insert(tmp_inx, self.get(it))
                            tmp_inx += 1
                        for it in reversed(range(tab.count)):
                            if it != int(tab_size/2)-1:
                                tab.delete1(it)
                            else:
                                break
                        if inx < sum(counts):
                            for it in range(len(counts)):
                                if inx - counts[it] < 0:
                                    tab.insert(inx, data)
                                    break
                        else:
                            counts.append(tab.next.count)
                            for it in range(len(counts)):
                                if inx - counts[it] < 0:
                                    tab.insert(inx, data)
                                    break
                        break

    def delete(self, inx: int):
        counts = []
        for tab in self.list:
            counts.append(tab.count)
            if sum(counts) > inx:
                it = 0
                while inx >= 0:
                    if inx - counts[it] < 0:
                        tab.delete1(inx)
                        if tab.count < int(tab_size / 2):
                            tab.insert(tab.count, tab.next.tab[0])
                            tab.next.delete1(0)
                            if tab.next.size < int(tab_size / 2):
                                for it in range(tab.next.count):
                                    tab.insert(tab.count, tab.next.tab[it])
                                    tab.next.delete1(it)
                                new_next = tab.next.next
                                tab.next = new_next
                        break
                    else:
                        inx -= counts[it]
                        it += 1
                break
        if inx > sum(counts):
            try:
                raise ValueError("wrong index!")
            except ValueError as err:
                print(err)

    def __str__(self):
        s = '['
        len_ = len(self.list)
        for tab in self.list:
            for it in range(tab.count):
                s += '{}'.format(tab.tab[it])
                if tab.tab[it] == tab.tab[tab.count - 1] and tab == self.list[len_-1]:
                    s += ']'
                else:
                    s += ', '
        return s


def main():
    test_list = Unrolled()

    for num in range(1, 10):
        test_list.insert(num-1, num)
    print(test_list)

    print(test_list.get(4))

    test_list.insert(1, 10)
    print(test_list)
    test_list.insert(8, 11)
    print(test_list)

    test_list.delete(1)
    test_list.delete(2)
    print(test_list)


main()
