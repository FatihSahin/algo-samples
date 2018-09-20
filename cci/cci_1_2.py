# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
# Hints: #7, #84, #722, #737 
import numpy as np

def isPermutation(str1, str2):
    strTuple = (str1, str2) if len(str1) <= len(str2) else (str2, str1)
    dictSmall = charFreq(strTuple[0])
    dictBig = charFreq(strTuple[1])
    for c in dictSmall:
        if c in dictBig:
            # check big str has enough of c chars for small str
            if not dictBig[c] >= dictSmall[c]:
                return False
        else:
            return False
    return True

def charFreq(str):
    dict1 = dict()
    for c in str:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1
    return dict1

print(isPermutation("loremdipsum", "ipsumdolorlorem"))


