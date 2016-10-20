"""
1.3 Given two strings, write a method to decide if one is a permutation of the other.
"""


def is_perm(str1, str2):
    if len(str1) != len(str2):
        return False

    cnt = dict()

    for c in str1:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1

    for c in str2:
        if c not in cnt:
            return False
        cnt[c] -= 1
        if cnt[c] == 0:
            cnt.pop(c)

    if len(cnt) > 0:
        return False

    return True


def main():
    print(is_perm('abcd', 'bcad'))
    print(is_perm('abcd1', 'bcad12'))
    print(is_perm('2abcd1', 'bcad12'))
    print(is_perm('2ebcd1', 'bcad12'))


if __name__ == '__main__':
    main()
