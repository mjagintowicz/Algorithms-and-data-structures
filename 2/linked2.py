#skonczone

class Elem:
    def __init__(self, data):
        self.data_ = data
        self.next_ = None
        self.prev_ = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def destroy(self):
        wsk = self.head
        self.head = None
        while wsk.next_ is not None:
            wsk.prev_ = None
            wsk = wsk.next_
        self.tail.prev_ = None
        self.tail = None

    def add(self, data):
        elem = Elem(data)
        if self.head is None and self.tail is None:
            self.head = elem
            self.tail = elem
        else:
            elem.next_ = self.head
            self.head.prev_ = elem
            self.head = elem

    def append(self, data):
        elem = Elem(data)
        if self.head is None and self.tail is None:
            self.head = elem
            self.tail = elem
        else:
            elem.prev_ = self.tail
            self.tail.next_ = elem
            self.tail = elem

    def remove(self):
        if self.head is not None and self.tail is not None:
            wsk = self.head
            wsk = wsk.next_
            wsk.prev_ = None
            self.head = wsk
        else:
            try:
                raise ValueError("empty list!!! - cant remove")
            except ValueError as err:
                print(err)

    def remove_end(self):
        if self.head is not None and self.tail is not None:
            wsk = self.head
            while wsk.next_ != self.tail:
                wsk = wsk.next_
            self.tail.prev_ = None
            wsk.next_ = None
            self.tail = wsk
        else:
            try:
                raise ValueError("empty list!!! - cant remove")
            except ValueError as err:
                print(err)

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def length(self):
        wsk = self.head
        n = 0
        while wsk is not None:
            wsk = wsk.next_
            n += 1
        return n

    def get(self):
        return self.head.data_

    def __str__(self):
        wsk = self.head
        s = ""
        while wsk is not None:
            s += "-> " + str(wsk.data_) + "\n"
            wsk = wsk.next_
        return s


def main():
    dane = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]

    uczelnie = LinkedList()

    uczelnie.append(dane[0])
    uczelnie.append(dane[1])
    uczelnie.append(dane[2])
    print(uczelnie)

    uczelnie.add(dane[3])
    uczelnie.add(dane[4])
    uczelnie.add(dane[5])

    print(uczelnie)

    print(uczelnie.length())

    uczelnie.remove()

    print(uczelnie.head.data_)

    uczelnie.remove_end()

    print(uczelnie)

    uczelnie.destroy()
    print(uczelnie.is_empty())

    uczelnie.remove()
    uczelnie.remove_end()


main()
