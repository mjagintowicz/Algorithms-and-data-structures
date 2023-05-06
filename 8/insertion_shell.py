# skonczone

import random
import time
import heap_selection


def insertion_sort(lst):
    lst_copy = lst[:]
    for i in range(len(lst_copy) - 1):
        if lst_copy[i+1] < lst_copy[i]:
            lst_copy[i+1], lst_copy[i] = lst_copy[i], lst_copy[i+1]
            j = i
            while j > 0 and j-1 >= 0 and lst_copy[j] < lst_copy[j-1]:
                lst_copy[j], lst_copy[j-1] = lst_copy[j-1], lst_copy[j]
                j -= 1
            i += 1
    return lst_copy


def insertion_sort_wo_copy(lst, gap=1):
    for i in range(gap):
        while i < len(lst) and i + gap < len(lst):
            if lst[i+gap] < lst[i]:
                lst[i+gap], lst[i] = lst[i], lst[i+gap]
                j = i
                while j > 0 and j-gap >= 0 and lst[j] < lst[j-gap]:
                    lst[j], lst[j-gap] = lst[j-gap], lst[j]
                    j -= gap
            i += gap
    return lst


def shell_sort(lst):
    lst_copy = lst[:]
    h = 1
    while h < len(lst_copy):
        h = 3*h + 1
    h //= 9
    sorted_ = False
    while not sorted_:
        lst_copy = insertion_sort_wo_copy(lst_copy, h)
        if h == 1:
            sorted_ = True
        h //= 3
    return lst_copy


def main():

    test = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]

    print(insertion_sort(test))
    print(shell_sort(test))

    print('Algorytmy stabilne')

    test_tab = [int(random.random() * 100) for i in range(10000)]
    t_start = time.perf_counter()
    insertion_sort(test_tab)
    t_stop = time.perf_counter()
    print("Czas obliczeń insertion sort:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    shell_sort(test_tab)
    t_stop = time.perf_counter()
    print("Czas obliczeń shell sort:", "{:.7f}".format(t_stop - t_start))

    test_heap = heap_selection.Queue(0, test_tab)
    t_start = time.perf_counter()
    while not test_heap.is_empty():
        test_heap.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń heap sort:", "{:.7f}".format(t_stop - t_start))


main()
