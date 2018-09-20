# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def isAllUnique(str):
    charSet = set()
    for c in str:
        if c in charSet:
            return False
        else:
            charSet.add(c)
    return True

#print(isAllUnique("fatih"))
print(isAllUnique('a'))