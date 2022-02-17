import random
from tracemalloc import start
from typing import List


def PossibleCombinations(Colors = ['A','B','C','D','E','F'], Positions = 4 ,Text = '', List = []):
    Positions = Positions - 1
    for i in Colors:
        Current = Text
        Current = Current + i
        if Positions > 0:
            List = PossibleCombinations(Colors, Positions,Current, List)
        else:
            List.append(Current)
    return List
    

def Feedback(CorrectCombinationStr,GuessStr):
    CorrectCombination = []
    Guess = []
    CorrectCombination.extend(CorrectCombinationStr)
    Guess.extend(GuessStr)
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

def EnterCode(MaxLength = 4):
    Colors = ['A','B','C','D','E','F']
    BadCode = True
    while BadCode:
        BadCode = False
        Code = input('Vul een code in met een lengte van '+str(MaxLength)+'.\nJe kun kiezen uit: A,B,C,D,E,F: ').upper()
        for i in Code:
            if not i in Colors or len(Code) != MaxLength:
                BadCode = True
    return Code

def UserFeedback(LengthCode):
    Colors = ['A','B','C','D','E','F']
    BadFeedback = True
    while BadFeedback:
        try:
            BlackPin = int(input('Geef aantal kleuren op juiste plek: '))
            WhitePin = int(input('Geef aantal kleuren op verkeerde plek: '))
            if not BlackPin + WhitePin > LengthCode:
                Feedback = [BlackPin,WhitePin]
                BadFeedback = False
        except ValueError:
            pass
    return Feedback
    

def GenerateMatrix(PossibleGuesses):
    Matrix = []
    for Index in range(len(PossibleGuesses)):
        Matrix.append([])
        for PossibleGuess in PossibleGuesses:
            Matrix[Index].append(Feedback(PossibleGuess, PossibleGuesses[Index]))
    return Matrix

def GeneratePossibleScores(CodeLength):
    PossibleScores = []
    for i in range(CodeLength+1):
        for x in range(CodeLength+1):
            if not i + x > CodeLength:
                PossibleScores.append([i,x])
    return PossibleScores

def GetAllIndex(List, Value):
    print(Value)
    Indexes = []
    for Index in range(len(List)):
        if List[Index] == Value:
            Indexes.append(Index)
    return Indexes


def FilterMatrix(PossibleGuesses, Matrix):
    FilteredMatrix = []
    PossibleScores = GeneratePossibleScores(len(PossibleGuesses[0]))
    for i in range(len(Matrix)):
        FilteredMatrix.append([])
        for Score in PossibleScores:
            FilteredMatrix[i].append(Matrix[i].count(Score))
        FilteredMatrix[i] = max(FilteredMatrix[i])
    Indexes = GetAllIndex(FilteredMatrix,min(FilteredMatrix))
    Guesses = []
    for Index in Indexes:
        Guesses.append(PossibleGuesses[Index])
    return Guesses


def GetPossibleGuesses(PossibleGuesses, GuessHistory, ScoreHistory):
    for Index in range(len(GuessHistory)):
            PossibleGuesses = FilterGuesses(PossibleGuesses, GuessHistory[Index], ScoreHistory[Index])
    return PossibleGuesses

def SimpleAlogrithm(PossibleGuesses, GuessHistory, ScoreHistory):
    if ScoreHistory != []:
        PossibleGuesses = GetPossibleGuesses(PossibleGuesses, GuessHistory, ScoreHistory)
    Guess = PickGuess(PossibleGuesses, GuessHistory)
    return Guess

def WorstCaseAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory):
    if ScoreHistory != []:
        PossibleGuesses = GetPossibleGuesses(PossibleGuesses, GuessHistory, ScoreHistory)
    Matrix = GenerateMatrix(PossibleGuesses)
    OptimalGuesses = FilterMatrix(PossibleGuesses,Matrix)
    Guess = PickGuess(OptimalGuesses,GuessHistory)
    return Guess
    


    



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
    Guess = ''
    PossibleGuesses = PossibleCombinations(List=[])
    Code = random.choice(PossibleGuesses)
    LengthCode = len(Code)
    GuessHistory = []
    ScoreHistory = []
    while Guess != Code:
        Guess = EnterCode(LengthCode)
        Score = Feedback(Code, Guess)
        GuessHistory.append(Guess)
        ScoreHistory.append(Score)
        for i in range(len(GuessHistory)):
            print(GuessHistory[i], ScoreHistory[i])
    print('WIN')



    

def Codemaker():
    Simple = False
    Worst = False
    while True:
        print('Codemaker')
        print("""
        Menu:
        
        1. Simple Algorithm
        2. Worst Case Algorithm
         """)
        UserInput = input('Maak een keuze: ')
        if UserInput == '1':
            Simple = True
            break
        elif UserInput == '2':
            Worst = True
            break
        else:
            print('Invalid input')
    LengthCode = 4
    Code = EnterCode(LengthCode)
    PossibleGuesses = PossibleCombinations(List=[], Positions=LengthCode)
    Guess = None
    Score = None
    GuessHistory = []
    ScoreHistory = []
    while Score != [LengthCode,0]:
        if Simple:
            Guess = SimpleAlogrithm(PossibleGuesses, GuessHistory, ScoreHistory)
        elif Worst:
            Guess = WorstCaseAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory)
        print('Code:',Code)
        print('Guess:',Guess)
        Score = UserFeedback(LengthCode)
        GuessHistory.append(Guess)
        ScoreHistory.append(Score)

def PickGuess(PossibleGuesses, GuessHistory):
    while True:
        Guess = random.choice(PossibleGuesses)
        if Guess not in GuessHistory:
            break
    return Guess

    
def Debug():
    Tries = 0
    Simple = False
    Worst = False
    while True:
        print('debug')
        print("""
        Menu:
        
        1. Simple Algorithm
        2. Worst Case Algorithm
         """)
        UserInput = input('Maak een keuze: ')
        if UserInput == '1':
            Simple = True
            break
        elif UserInput == '2':
            Worst = True
            break
        else:
            print('Invalid input')
    LengthCode = 4
    PossibleGuesses = PossibleCombinations(List=[], Positions=LengthCode)
    Code = random.choice(PossibleGuesses)
    Guess = None
    Score = None
    GuessHistory = []
    ScoreHistory = []
    while Score != [LengthCode,0]:
        Tries += 1
        if Simple:
            Guess = SimpleAlogrithm(PossibleGuesses, GuessHistory, ScoreHistory)
        elif Worst:
            Guess = WorstCaseAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory)
        Score = Feedback(Code,Guess)
        GuessHistory.append(Guess)
        ScoreHistory.append(Score)
    print("Pogingen:", Tries)
    

def FilterGuesses(PossibleGuesses, GuessStr, Score):
    Guess = []
    Guess.extend(GuessStr)
    result = []
    for PossibleGuess in PossibleGuesses:
        PossibleScore = Feedback(GuessStr, PossibleGuess)
        if PossibleScore == Score:
            result.append(PossibleGuess)
    return result

Start()