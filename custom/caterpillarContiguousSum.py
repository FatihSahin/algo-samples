# Let’s check whether a sequence a0, a1,...,an≠1 (1 ˛ ai ˛ 109) contains a contiguous subsequence
# whose sum of elements equals s. For example, in the following sequence we are looking
# for a subsequence whose total equals s = 12.

def caterpillarMethod(A, s):
    n = len(A)
    front, total = 0, 0
    for back in range(n):
        while (front < n and total + A[front] <= s):
            total += A[front]
            front += 1
        if total == s:
            return True
        total -= A[back]
    return False

print(caterpillarMethod([6,2,7,4,1,3,6], 12))