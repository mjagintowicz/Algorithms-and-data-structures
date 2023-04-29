# skonczone

import random
import time


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

    def __init__(self, size=0, tab_to_sort=[]):
        if tab_to_sort:
            self.heap_size = len(tab_to_sort)
            self.size = len(tab_to_sort)
            self.tab = tab_to_sort
            self.heapify()
        else:
            self.heap_size = 0
            self.size = size
            self.tab = [None for i in range(size)]

    def heapify(self):
        if self.tab:
            start_inx = self.parent(len(self.tab) - 1)
            for i in reversed(range(start_inx+1)):
                self.repair_dequeue(i)

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

    def dequeue(self, inx=0):
        if self.is_empty():
            return None
        else:
            elem = self.tab[0]
            if self.heap_size != 1:
                self.tab[inx], self.tab[self.heap_size - 1] = self.tab[self.heap_size - 1], self.tab[inx]
                self.heap_size -= 1
                self.repair_dequeue()
            else:
                self.heap_size -= 1
            return elem

    def repair_dequeue(self, inx=0):
        node = self.tab[inx]
        greater_child = None
        if self.right(inx) < self.heap_size and self.left(inx) < self.heap_size - 1:
            if self.tab[self.right(inx)] > self.tab[self.left(inx)]:
                greater_child = self.tab[self.right(inx)]
                gr_inx = self.right(inx)
            else:
                greater_child = self.tab[self.left(inx)]
                gr_inx = self.left(inx)
        elif self.left(inx) < self.heap_size <= self.right(inx):
            greater_child = self.tab[self.left(inx)]
            gr_inx = self.left(inx)
        if greater_child is not None:
            while greater_child > node:
                self.tab[inx], self.tab[gr_inx] = self.tab[gr_inx], self.tab[inx]
                inx = gr_inx
                if self.right(inx) >= self.size or self.left(inx) >= self.size:
                    break
                if self.right(inx) < self.heap_size and self.left(inx) < self.heap_size - 1:
                    if self.tab[self.right(inx)] > self.tab[self.left(inx)]:
                        greater_child = self.tab[self.right(inx)]
                        gr_inx = self.right(inx)
                    else:
                        greater_child = self.tab[self.left(inx)]
                        gr_inx = self.left(inx)
                elif self.left(inx) < self.heap_size <= self.right(inx):
                    greater_child = self.tab[self.left(inx)]
                    gr_inx = self.left(inx)
                else:
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

    def print_heap(self):
        print('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)

    def print_tab(self):
        print(self.tab)


def selection_swap(tab):
    copy_tab = tab[:]
    for i in range(len(copy_tab)-1):
        min = copy_tab[i]
        min_inx = i
        for j in range(i, len(copy_tab)):
            if copy_tab[j] < min:
                min = copy_tab[j]
                min_inx = j
        copy_tab[i], copy_tab[min_inx] = copy_tab[min_inx], copy_tab[i]
    return copy_tab


def selection_shift(tab):
    copy_tab = tab[:]
    for i in range(len(copy_tab) - 1):
        min = copy_tab[i]
        min_inx = i
        for j in range(i, len(copy_tab)):
            if copy_tab[j] < min:
                min = copy_tab[j]
                min_inx = j
        copy_tab.pop(min_inx)
        copy_tab.insert(i, min)
    return copy_tab


def main():

    tab_to_sort = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    heap = Queue(0, tab_to_sort)

    heap.print_heap()
    heap.print_tree(0, 0)

    while not heap.is_empty():
        heap.dequeue()

    heap.print_tab()

    test_tab = [int(random.random() * 100) for i in range(10000)]
    test_heap = Queue(0, test_tab)
    t_start = time.perf_counter()
    while not test_heap.is_empty():
        test_heap.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    print(selection_swap(tab_to_sort))
    print(selection_shift(tab_to_sort))

    test_tab_swap = [int(random.random() * 100) for i in range(10000)]
    t_start = time.perf_counter()
    selection_swap(test_tab_swap)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    test_tab_shift = [int(random.random() * 100) for i in range(10000)]
    t_start = time.perf_counter()
    selection_swap(test_tab_shift)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


main()
