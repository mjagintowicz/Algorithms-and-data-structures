#skonczone

def realloc(tab, size):
    oldsize = len(tab)
    return [tab[i] if i < oldsize else None for i in range(size)]


class Queue:
    def __init__(self):
        self.size = 5
        self.tab = [None for i in range(self.size)]
        self.inx_w = 0
        self.inx_r = 0

    def is_empty(self):
        if self.inx_w == self.inx_r:
            return True
        else:
            return False

    def peek(self):
        if self.inx_w == self.inx_r:
            return None
        else:
            return self.tab[self.inx_r]

    def dequeue(self):
        if self.inx_w == self.inx_r:
            return None
        else:
            el = self.tab[self.inx_r]
            self.tab[self.inx_r] = None
            if self.inx_r == self.size - 1:
                self.inx_r = 0
            else:
                self.inx_r += 1
            return el

    def enqueue(self, data):
        self.tab[self.inx_w] = data
        if self.inx_w == self.size - 1:
            self.inx_w = 0
        else:
            self.inx_w += 1
        if self.inx_w == self.inx_r:
            oldsize = self.size
            self.size *= 2
            new_tab = realloc(self.tab, self.size)
            for it in range(self.inx_r, oldsize):
                new_tab[it + oldsize] = new_tab[it]
                new_tab[it] = None
            self.tab = new_tab
            self.inx_r += oldsize

    def __str__(self):
        s = "["
        if self.inx_w == self.inx_r:
            pass
        elif self.inx_r < self.inx_w:
            for it in range(self.inx_r, self.inx_w):
                s += '{}'.format(self.tab[it])
                if it == self.inx_w - 1:
                    break
                s += ", "
        else:
            for it in range(self.inx_r, self.size):
                s += '{}'.format(self.tab[it])
                s += ", "
            for it in range(self.inx_w):
                s += '{}'.format(self.tab[it])
                if it == self.inx_w - 1:
                    break
                s += ", "
        s += "]"
        return s


def main():
    new_queue = Queue()

    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    new_queue.enqueue(4)

    print(new_queue.dequeue())

    print(new_queue.peek())

    print(new_queue)

    new_queue.enqueue(5)
    new_queue.enqueue(6)
    new_queue.enqueue(7)
    new_queue.enqueue(8)

    print(new_queue.tab)

    while not new_queue.is_empty():
        print(new_queue.dequeue())

    print(new_queue)


main()
