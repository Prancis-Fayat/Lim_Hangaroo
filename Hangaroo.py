from isWordGuessed import isWordGuessed
from getGuessedWord import getGuessedWord
from getAvailableLetters import getAvailableLetters
def hangaroo(secretWord): 
        print("Welcome to Hangaroo!")
        print("The word is ", len(secretWord), "letters long")
        secretWord=secretWord.lower()
        secretWord=list(secretWord)
        lettersGuessed=[]
        wordCheck=isWordGuessed(secretWord,lettersGuessed)
        mistakesMade=0
        while wordCheck == False:
            wordCheck=isWordGuessed(secretWord,lettersGuessed)
            guess=input('Guess a letter:')
            guess = guess.lower()
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print(getGuessedWord(secretWord, lettersGuessed), 'Available letters:', getAvailableLetters(lettersGuessed))
                wordCheck=isWordGuessed(secretWord,lettersGuessed)
            elif guess not in secretWord and guess not in lettersGuessed:
                print("wrong guess, input again")
                mistakesMade += 1 
        else :
            print('you win!')
            print('number of mistakes made', mistakesMade)
            return print('Game Over!','The answer is:',secretWord, 'Your guessed letters are:',lettersGuessed)
    
            
            
