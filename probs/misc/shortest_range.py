"""
You have k lists of sorted integers. Find the smallest range that includes at least one number from
each of the k lists.

For example,
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]

The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2,
and 22 from list 3
"""
import sys


def solve(k_lists):
    inds = [0] * len(k_lists)
    min_range = sys.maxsize, None

    while True:
        elems = [lst[inds[i]] for i, lst in enumerate(k_lists)]

        mine = min(elems)
        mini = elems.index(mine)
        maxe = max(elems)

        rng = maxe - mine
        if rng < min_range[0]:
            min_range = rng, (mine, maxe)

        inds[mini] += 1

        if len(k_lists[mini]) == inds[mini]:
            break

    return min_range[1]


if __name__ == '__main__':
    a = [4, 10, 15, 24, 26]
    b = [0, 9, 12, 20]
    c = [5, 18, 22, 30]
    rng = solve([a, b, c])
    print(rng)
