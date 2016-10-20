"""
1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?

I/p
1 2 3
4 5 6
7 8 9

o/p
7 4 1
8 5 2
9 6 3

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""


def im_rot90(img):
    n = len(img)

    for layer in range(n // 2):
        for i in range(layer, n-1-layer):
            tmp = img[layer][i]
            img[layer][i] = img[n-1-i][layer]
            img[n-1-i][layer] = img[n-1-layer][n-1-i]
            img[n-1-layer][n-1-i] = img[i][n-1-layer]
            img[i][n-1-layer] = tmp


def main():
    # img = [[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]]
    img = [[i for i in range(1, 6)] for _ in range(5)]
    print(img)
    im_rot90(img)
    print(img)


if __name__ == '__main__':
    main()
