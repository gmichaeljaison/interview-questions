"""
 Numbers are randomly generated and stored into an (expanding) array.
 How would you keep track of the median?
"""

import heapq


class MedianTrack:
    def __init__(self):
        # min heap for last half of numbers
        self.right_min_heap = list()
        # max heap for first half of numbers
        # All numbers are negated to use min-heap as max-heap
        self.left_max_heap = list()

    def add_number(self, n):
        if len(self.left_max_heap) == 0:
            heapq.heappush(self.left_max_heap, -n)
            return

        if len(self.left_max_heap) == len(self.right_min_heap):
            # next slot is left heap
            if n > self.right_min_heap[0]:
                n = heapq.heapreplace(self.right_min_heap, n)

            heapq.heappush(self.left_max_heap, -n)
        else:
            # next slot is right heap
            if n < -self.left_max_heap[0]:
                n = -heapq.heapreplace(self.left_max_heap, -n)

            heapq.heappush(self.right_min_heap, n)

    def median(self):
        if len(self.left_max_heap) == 0:
            return 0

        if len(self.left_max_heap) == len(self.right_min_heap):
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2

        return -self.left_max_heap[0]


def main():
    numbers = [5, 4, 10, 2, 5, 1, 3]
    med = MedianTrack()

    for n in numbers:
        med.add_number(n)
        print(med.median())


if __name__ == '__main__':
    main()
