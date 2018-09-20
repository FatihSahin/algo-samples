# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

# Some initial algorithm design is as follows, use adjecent couple and calclulate best alternative with next adjecent couple
# Keep track of the best double from these couples accumlating total, also keep track of alternative double as it may accumulate more 
# as you slide the coupling index. Avoid negative and zero integers at all costs. Just skip them.

def calculateMaxSumForNotAdjacents(arr):
    length = len(arr)
    result = list()
    isLefty = True
    i = 0
    while i < length:
        if arr[i] <= 0:
            continue
        if i + 1 < length:
            if arr[i] > arr[i + 1]:
                result.append(arr[i])
                isLefty = True
            elif arr[i+1] > 0:
                result.append(arr[i+1])
                isLefty = False
    return result   



calculateMaxSumForNotAdjacents([12,4,1,12,23,1])  # Should return [12, 1, 23]