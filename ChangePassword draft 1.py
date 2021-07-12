import math
def matchPasswordWithSystem(password):
    matches = verifyPassword(password)
    return matches

def verifyPassword(password):
    specialChars = ['!',"@","#","$","&","*"]
    if len(password)<18:
        return False
    oneUpperCase = False
    oneLowerCase = False
    countSpecialChar = 0
    countDigit = 0
    charDict = {}
    for i in password:
        if i in charDict:
            charDict[i]+=1
        else:
            charDict[i]=1
    maxValue = max(x for x in charDict.values())
    if maxValue > 4:
        return False
    for i in charDict.keys():
        if i in specialChars:
            countSpecialChar+=charDict[i]
    for i in charDict.keys():
        if 64<ord(i)<91:
            oneUpperCase = True
            break
    for i in charDict.keys():
        if 96<ord(i)<123:
            oneLowerCase = True
            break
    for i in charDict.keys():
        if 47<ord(i)<58:
            countDigit+=charDict[i]
    if not oneLowerCase or not oneUpperCase or not countSpecialChar or not countDigit:
        return False
    if countSpecialChar > 4 or countDigit >= len(password)/2:
        return False
    return True

def checkSimilarity(oldPassword, newPassword):
    if oldPassword == newPassword:
        return False
    charDictOld = {}
    for i in oldPassword:
        if i in charDictOld:
            charDictOld[i]+=1
        else:
            charDictOld[i]=1
    charDictNew = {}
    for i in newPassword:
        if i in charDictNew:
            charDictNew[i]+=1
        else:
            charDictNew[i]=1
    similarCount = 0
    for i in charDictOld.keys():
        if i in charDictNew:
            similarCount += charDictOld[i] if charDictOld[i]<charDictNew[i] else charDictNew[i]
    if math.ceil(len(oldPassword)*4/5)<= similarCount:
        return False
    return True


def changePassword(oldPassword, newPassword):
    flag = matchPasswordWithSystem(oldPassword)
    if not flag:
        print("oldPassword does not match with system")
        return False
    flag = verifyPassword(newPassword)
    if not flag:
        print("newPassword is not a valid password")
        return False
    flag = checkSimilarity(oldPassword, newPassword)
    if not flag:
        print("newPassword is too similar to the old password")
        return False
    flag = checkSimilarity(newPassword, oldPassword)
    if not flag:
        print("newPassword is too similar to the old password")
        return False
    return True


print(changePassword("abcdefABCDEF@!#$123456","qwerrtyABCDEF@!#$1"))
