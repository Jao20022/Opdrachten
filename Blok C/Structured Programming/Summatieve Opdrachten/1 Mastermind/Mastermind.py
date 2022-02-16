from __future__ import barry_as_FLUFL
import random


def PossibleCombinations(Colors = ['A','B','C','D','E','F'], Positions = 4 ,Text = '', List = []):
    Positions = Positions - 1
    for i in Colors:
        Current = Text
        Current = Current + i
        if Positions > 0:
            List = PossibleCombinations(Colors, Positions,Current, List)
        else: List.append(Current)
    return List
    
def StringtoArray(String):
    List = []
    for Letter in String:
        List.append(Letter)
    return List

def Feedback(CorrectCombinationStr,GuessStr):
    CorrectCombination = StringtoArray(CorrectCombinationStr)
    Guess = StringtoArray(GuessStr)
    Feedback = [0,0]
    i = 0
    while i < len(CorrectCombination) > 0:
        if CorrectCombination[i] == Guess[i]:
            Feedback[0] = Feedback[0] + 1
            CorrectCombination.pop(i)
            Guess.pop(i)
            i = 0
        else:
            i = i+1
    i = 0
    while i < len(CorrectCombination) > 0:
        if Guess[i] in CorrectCombination:
            Feedback[1] = Feedback[1] + 1
            CorrectCombination.pop(CorrectCombination.index(Guess[i]))
            Guess.pop(i)
            i = 0
        else:
            i = i+1
    return Feedback

def EnterCode():
    BadCode = True
    while BadCode:
        BadCode = False
        Code = input('Vul een code in met een lengte van 4.\nJe kun kiezen uit: A,B,C,D,E,F: ').upper()
        for i in Code:
            if not i in Colors or len(Code) != 4:
                BadCode = True
    return Code

def SimpleAlogrithm():
    x = 5



def Start():
    while True:
        print("""
        Menu:
        
        1. Codebreaker
        2. Codemaker
        3. Debug
         """)
        UserInput = input('Maak een keuze: ')
        if UserInput == '1':
            Codebreaker()
        elif UserInput == '2':
            Codemaker()
        elif UserInput == '3':
            Debug()
        else:
            print('Invalid input')


def Codebreaker():
    print('Codebreaker')

def Codemaker():
    print('Codemaker')
    Code = EnterCode()
    PossibleGuesses = PossibleCombinations()
    Guess = ''
    while Guess != Code:
        break


def PickGuess(PossibleGuesses, Guesses):
    while True:
        Guess = random.choice(PossibleGuesses)
        if Guess not in Guesses:
            break
    return Guess

    
def Debug():
    PossibleGuesses = PossibleCombinations()
    Code = random.choice(PossibleGuesses)
    Guess = ''
    Guesses = []
    Scores = []
    while Guess != Code:
        print(len(PossibleGuesses))
        if not Code in PossibleGuesses:
            print('Error')
            break
        Guess = PickGuess(PossibleGuesses, Guesses)
        Score = Feedback(Code, Guess)
        Guesses.append(Guess)
        Scores.append(Score)
        PossibleGuesses = FilterGuesses(PossibleGuesses, Code, Guess, Score)
    print(Code)
    print(Guess)
    print('win')
    

def FilterGuesses(PossibleGuesses,Code, GuessStr, Score):
    Guess = StringtoArray(GuessStr)
    result = []
    for PossibleGuess in PossibleGuesses:
        PossibleScore = Feedback(Code, PossibleGuess)
        if not PossibleScore < Score:
            result.append(PossibleGuess)
    return result

Start()