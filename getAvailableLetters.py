import string
alphabet = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):

    remain = []
    for x in alphabet:
        if x not in lettersGuessed:
            remain.append(x)
    return ''.join(remain)  