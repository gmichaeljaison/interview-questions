def filter_th(arr, th):
    return [x for x in arr if x <= th]


def remove_val(arr, val):
    arr_c = arr[:]
    arr_c.remove(val)
    return arr_c


def max_valid_time(arr):
    h1_list = filter_th(arr, 2)
    h1_list.sort(reverse=True)

    res = [0] * 4

    for h1 in h1_list:
        res[0] = h1

        arr_3 = remove_val(arr, h1)
        h2_list = arr_3[:]
        if h1 == 2:
            h2_list = filter_th(h2_list, 3)
        h2_list.sort(reverse=True)

        for h2 in h2_list:
            res[1] = h2

            arr_2 = remove_val(arr_3, h2)
            m1_list = filter_th(arr_2, 5)

            for m1 in m1_list:
                res[2] = m1

                m2_list = remove_val(arr_2, m1)

                if len(m2_list) == 0:
                    continue

                res[3] = m2_list[0]
                return '{}{}:{}{}'.format(*res)

    return "NOT POSSIBLE"


if __name__ == '__main__':
    a = [9, 2, 1, 9]
    print(max_valid_time(a))

    print(max_valid_time([1, 8, 3, 2]))

    print(max_valid_time([2, 4, 0, 0]))

    print(max_valid_time([3, 0, 7, 0]))

    print(max_valid_time([9, 1, 9, 7]))

    print(max_valid_time([0, 0, 0, 0]))
    print(max_valid_time([9] * 4))
    print(max_valid_time([2, 4, 1, 1]))
