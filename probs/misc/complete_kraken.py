"""
Ways to complete kraken
"""


def ways_to_kraken(m, n):
    res = [[1 for _ in range(n)] for _ in range(m)]

    for row in range(m):
        for col in range(n):
            if col == 0 or row == 0:
                continue

            res[row][col] = res[row-1][col] + res[row][col-1] + res[row-1][col-1]
    return res


def main():
    m = int(input().strip())
    n = int(input().strip())
    res = ways_to_kraken(m, n)
    # print(res)
    print(res[-1][-1])


if __name__ == '__main__':
    main()
