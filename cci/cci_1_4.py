# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

def isPalindromePerm(txt):
    """
    if it has a total of even number of chars, all chars must be even number on its own.
    if it has a total of odd number of chars, only one char has to be in odd numbers.
    """
    chars = txt.lower().replace(' ', '')
    isOdd = len(chars) % 2 == 1
    charDict = dict()
    #count char counts
    for ch in chars:
        if ch in charDict:
            charDict[ch] += 1
        else:
            charDict[ch] = 1
    
    singles = sum(1 for (key, val) in charDict.items() if val % 2 == 1)
    return singles == 1 if isOdd else singles == 0
    
print(isPalindromePerm("Tact Coolla")) #True