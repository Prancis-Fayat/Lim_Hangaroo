def getGuessedWord(secretWord, lettersGuessed): 
    result = []
    for x in secretWord:
        if x in lettersGuessed:
            result.append(x)
        else:
            result.append('_')
    return ' '.join(result)
