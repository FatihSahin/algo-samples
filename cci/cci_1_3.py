# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def urlify(st, trueLen):
    strNew = []
    takeLen = trueLen
    for i, item in enumerate(st):
        if item == ' ':
            strNew.append('%')
            strNew.append('2')
            strNew.append('0')
            if i < trueLen:
                takeLen += 2
        else:
            strNew.append(item)

    return ''.join(strNew[:takeLen])


print(urlify("Mr John Smith    ", 13))