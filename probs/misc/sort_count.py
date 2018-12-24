import sys


def solution(A):
    i_pos = -1
    j_pos = -1
    k_pos = -1
    mismatch_cnt = 0
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            i_pos = i
            break

    for j in range(len(A) - 1, 0, -1):
        if A[j] < A[j - 1]:
            j_pos = j
            break

    for k in range(i_pos, len(A) - 1):
        if A[k] > A[i_pos]:
            k_pos = k - 1
            break

    if i_pos != -1 and j_pos != -1:
        mismatch_cnt = max(mismatch_cnt, max(j_pos, k_pos) - i_pos + 1)
    return mismatch_cnt


print(solution([1]))
print(solution([1, 2]))
print(solution([3, 2]))
print(solution([10, 9, 8, 7, 5, 4, 3, 2, 1]))
print(solution([1, 2, 6, 5, 5, 8, 9, 4, 10]))
print(solution([1, 2, 6, 5, 5, 8, 9, 4, 10]))
print(solution([10, 9, 8, 7, 5, 4, 3, 2, 1, 0]))
