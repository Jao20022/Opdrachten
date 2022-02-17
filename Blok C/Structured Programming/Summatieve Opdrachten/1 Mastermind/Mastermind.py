import random


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
        PossibleGuesses = FilterGuesses(PossibleGuesses, Guess, Score)
    print(Code)
    print(Guess)
    print('win')

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





def WorstCaseAlgorithm():
    PossibleGuesses = PossibleCombinations()
    Code = random.choice(PossibleGuesses)
    Guess = ''
    GuessHistory = []
    ScoreHistory = []
    while Guess != Code:
        print(len(PossibleGuesses))
        if not Code in PossibleGuesses:
            print('Error')
            break
        Matrix = GenerateMatrix(PossibleGuesses)
        OptimalGuesses = FilterMatrix(PossibleGuesses,Matrix)
        Guess = PickGuess(OptimalGuesses,GuessHistory)
        Score = Feedback(Code, Guess)
        GuessHistory.append(Guess)
        ScoreHistory.append(Score)
        PossibleGuesses = FilterGuesses(PossibleGuesses, Guess, Score)
    print(Code)
    print(Guess)
    print('win')
    



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


def PickGuess(PossibleGuesses, GuessHistory):
    while True:
        Guess = random.choice(PossibleGuesses)
        if Guess not in GuessHistory:
            break
    return Guess

    
def Debug():
    while True:
        print("""
        Menu:
        
        1. Simple Algorithm
         """)
        UserInput = input('Maak een keuze: ')
        if UserInput == '1':
            SimpleAlogrithm()
        elif UserInput == '2':
            Codemaker()
        elif UserInput == '3':
            Debug()
        else:
            print('Invalid input')
    

def FilterGuesses(PossibleGuesses, GuessStr, Score):
    Guess = []
    Guess.extend(GuessStr)
    result = []
    for PossibleGuess in PossibleGuesses:
        PossibleScore = Feedback(GuessStr, PossibleGuess)
        if PossibleScore == Score:
            result.append(PossibleGuess)
    return result

WorstCaseAlgorithm()