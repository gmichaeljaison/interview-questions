import numpy as np


if __name__ == '__main__':
    data = np.loadtxt('test1', delimiter='\t', dtype=str)
    print(len(data))

    fl_data = data.copy()
    missing_rows = list()
    for row in range(len(data)):
        if 'Missing' in data[row][1]:
            missing_rows.append(row)
            fl_data[row, 1] = -1
        else:
            val = fl_data[row, 1][2:-1]
            fl_data[row, 1] = val

    fl_data = fl_data[:, 1]

    print(fl_data[1:10])

    fl_data = fl_data.astype(float)
    fl_data = fl_data[fl_data > 0]

    print(len(fl_data))

    print(fl_data.mean())
