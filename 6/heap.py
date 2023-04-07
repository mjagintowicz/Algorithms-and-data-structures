# skonczone

class Elem:

    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __le__(self, other):
        return self.__priorytet <= other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet

    def __ge__(self, other):
        return self.__priorytet >= other.__priorytet

    def __str__(self):
        s = '{}'.format(self.__priorytet)
        s += ' : '
        s += '{}'.format(self.__dane)
        return s


class Queue:

    def __init__(self, size):
        self.heap_size = 0
        self.size = size
        self.tab = [None for i in range(size)]

    def is_empty(self):
        if self.heap_size == 0:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            elem = self.tab[0]
            if self.heap_size != 1:
                self.repair_dequeue()
            self.heap_size -= 1
            return elem

    def repair_dequeue(self, inx=0):
        self.tab[inx], self.tab[self.heap_size-1] = self.tab[self.heap_size-1], self.tab[inx]
        node = self.tab[inx]
        greater_child = None
        if self.tab[self.right(inx)] > self.tab[self.left(inx)]:
            if self.right(inx) < self.heap_size-1:
                greater_child = self.tab[self.right(inx)]
                gr_inx = self.right(inx)
            elif self.left(inx) < self.heap_size-1:
                greater_child = self.tab[self.left(inx)]
                gr_inx = self.left(inx)
        elif self.tab[self.right(inx)] < self.tab[self.left(inx)]:
            greater_child = self.tab[self.left(inx)]
            gr_inx = self.left(inx)
        if greater_child is not None:
            while greater_child > node:
                self.tab[inx], self.tab[gr_inx] = self.tab[gr_inx], self.tab[inx]
                inx = gr_inx
                if self.right(inx) >= self.size or self.left(inx) >= self.size:
                    break
                if self.tab[self.right(inx)] > self.tab[self.left(inx)]:
                    greater_child = self.tab[self.right(inx)]
                    gr_inx = self.right(inx)
                elif self.tab[self.right(inx)] <= self.tab[self.left(inx)]:
                    greater_child = self.tab[self.left(inx)]
                    gr_inx = self.left(inx)
                if gr_inx >= self.heap_size-1:
                    break

    def enqueue(self, data, priority):
        elem = Elem(data, priority)
        if self.heap_size == self.size:
            self.heap_size += 1
            self.size += 1
            self.tab.append(elem)
        else:
            self.heap_size += 1
            self.tab[self.heap_size-1] = elem
        child_inx = self.heap_size - 1
        parent_inx = self.parent(child_inx)
        if parent_inx >= 0:
            while self.tab[parent_inx] < elem:
                self.tab[self.parent(child_inx)], self.tab[child_inx] = self.tab[child_inx], self.tab[self.parent(child_inx)]
                child_inx = parent_inx
                parent_inx = self.parent(child_inx)
                if parent_inx < 0:
                    break

    def left(self, inx):
        return 2*inx + 1

    def right(self, inx):
        return 2*inx + 2

    def parent(self, inx):
        return (inx-1) // 2

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def main():
    queue = Queue(5)
    priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    values = ['G', 'R', 'Y', 'M', 'O', 'T', 'Y', 'L', 'A']
    for it in range(len(priorities)):
        queue.enqueue(values[it], priorities[it])
    queue.print_tree(0, 0)
    queue.print_tab()

    data = queue.dequeue()
    print(queue.peek())

    queue.print_tab()
    print(data)

    while queue.is_empty() is False:
        print(queue.dequeue())

    queue.print_tab()


main()
