import random


def Codebreaker():
    """
    Play the Game as Codebreaker

    Returns: None
    """
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
    """
    Play the Game as Codemaker

    Returns: None
    """
    Simple = False
    Worst = False
    Own = False
    while True:
        print('Codemaker')
        print("""
        Menu:
        
        1. Simple Algorithm
        2. Worst Case Algorithm
        3. Own Algorithm
         """)
        UserInput = input('Maak een keuze: ')
        if UserInput == '1':
            Simple = True
            break
        elif UserInput == '2':
            Worst = True
            break
        elif UserInput == '3':
            Own = True
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
    while Score != [LengthCode, 0]:
        if Simple:
            Guess = SimpleAlogrithm(PossibleGuesses, GuessHistory, ScoreHistory)
        elif Worst:
            Guess = WorstCaseAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory)
        elif Own:
            Guess = OwnAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory)
        print('Code:', Code)
        print('Guess:', Guess)
        Score = UserFeedback(LengthCode)
        GuessHistory.append(Guess)
        ScoreHistory.append(Score)


def Debug(Simple=False,Worst=False,Own=False):
    """
    Makes the Computer play against itself. Used for Debugging.
    Uses different algorithms based on the given boolean.


    Args:
        Simple: Boolean
        Worst: Boolean
        Own: Boolean

    Returns: Integer. ammount of turns for the correct code to be found
    """
    Tries = 0
    LengthCode = 4
    PossibleGuesses = PossibleCombinations(List=[], Positions=LengthCode)
    Code = random.choice(PossibleGuesses)
    Guess = None
    Score = None
    GuessHistory = []
    ScoreHistory = []
    while Score != [LengthCode, 0]:
        Tries += 1
        if Simple:
            Guess = SimpleAlogrithm(PossibleGuesses, GuessHistory, ScoreHistory)
        elif Worst:
            Guess = WorstCaseAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory)
        elif Own:
            Guess = OwnAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory)
        Score = Feedback(Code, Guess)
        GuessHistory.append(Guess)
        ScoreHistory.append(Score)
    return Tries


def EnterCode(MaxLength=4):
    """
    Let's the player enter a code, and checks the input.

    Args:
        MaxLength: Integer. Length of the Code

    Returns: String. A code
    """
    Colors = ['A', 'B', 'C', 'D', 'E', 'F']
    BadCode = True
    while BadCode:
        BadCode = False
        Code = input(
            'Vul een code in met een lengte van ' + str(MaxLength) + '.\nJe kun kiezen uit: A,B,C,D,E,F: ').upper()
        for i in Code:
            if not i in Colors or len(Code) != MaxLength:
                BadCode = True
    return Code


def Feedback(CorrectCombinationStr, GuessStr):
    """
    Checks the given Guess against the Code

    Args:
        CorrectCombinationStr: String. The correct code
        Guesstr: String. The guess

    Returns: List. Score
    """
    CorrectCombination = []
    Guess = []
    CorrectCombination.extend(CorrectCombinationStr)
    Guess.extend(GuessStr)
    Feedback = [0, 0]
    i = 0
    while i < len(CorrectCombination) > 0:
        if CorrectCombination[i] == Guess[i]:
            Feedback[0] = Feedback[0] + 1
            CorrectCombination.pop(i)
            Guess.pop(i)
            i = 0
        else:
            i = i + 1
    i = 0
    while i < len(CorrectCombination) > 0:
        if Guess[i] in CorrectCombination:
            Feedback[1] = Feedback[1] + 1
            CorrectCombination.pop(CorrectCombination.index(Guess[i]))
            Guess.pop(i)
            i = 0
        else:
            i = i + 1
    return Feedback


def FilterGuesses(PossibleGuesses, GuessStr, Score):
    """
    Filters the possible guesses according to the most recent Guess and coresponding Score.

    Args:
        PossibleGuesses: List. Possible Guesses
        GuessStr: String. Last Guess
        Score: List. Score of the Last Guess
    
    Returns: List. Possible next guesses
    """
    Guess = []
    Guess.extend(GuessStr)
    result = []
    for PossibleGuess in PossibleGuesses:
        PossibleScore = Feedback(GuessStr, PossibleGuess)
        if PossibleScore == Score:
            result.append(PossibleGuess)
    return result


def FilterMatrix(PossibleGuesses, Matrix, Filter = False):
    """
    Takes the matrix and returns a list of guesses with the lowest high ammount of guesses.
    

    Args:
        PossibleGuesses: List. Possible Guesses
        Matrix: List. All possible scores for all possible guesses.
        Filter: Boolean.

    Returns: List. Optimal guesses.
    """
    FilteredMatrix = []
    PossibleScores = GeneratePossibleScores(len(PossibleGuesses[0]), Filter)
    for i in range(len(Matrix)):
        FilteredMatrix.append([])
        for Score in PossibleScores:
            FilteredMatrix[i].append(Matrix[i].count(Score))
        FilteredMatrix[i] = max(FilteredMatrix[i])
    Indexes = GetAllIndex(FilteredMatrix, min(FilteredMatrix))
    Guesses = []
    for Index in Indexes:
        Guesses.append(PossibleGuesses[Index])
    return Guesses


def GenerateMatrix(PossibleGuesses):
    """
    
    Generates all possible Scores for significantly different PossibleGuesses

    Args:
        PossibleGuesses: List. All possible guesses.

    Returns: List. All possible scores for all possibleGuesses 
    
    """
    FirstCharacter = PossibleGuesses[0][0]
    FilteredGuesses = []
    for i in PossibleGuesses:
        if i[0] == FirstCharacter and reversed(i) not in FilteredGuesses:
            FilteredGuesses.append(i)
    Matrix = []
    for Index in range(len(FilteredGuesses)):
        Matrix.append([])
        for PossibleGuess in FilteredGuesses:
            Matrix[Index].append(Feedback(PossibleGuess,FilteredGuesses[Index]))
    return Matrix


def GeneratePossibleScores(CodeLength, Filter):
    """
    Generates a list of all possible Scores
    if Filter, only scores that do not contain a 0 or equals the codelength are returned.
    Args:
        CodeLength: Integer. Length of the code
        Filter: Boolean. Decides if the filter is applied.
    
    Returns: List. Of all possible scores
    """
    PossibleScores = []
    for i in range(CodeLength + 1):
        for x in range(CodeLength + 1):
            if Filter:
                if (i != 0 or x != 0) or i + x == CodeLength:
                    PossibleScores.append([i,x])
            else:
                if not i + x > CodeLength:
                    PossibleScores.append([i, x])
    return PossibleScores


def GetAllIndex(List, Value):
    """
    Gets all the indexes from a list with the given value.

    Args:
        List: List. That gets searched
        Value: Item for which the indexes get searched.
    
    Returns: List. Of all the indexes
    """
    Indexes = []
    for Index in range(len(List)):
        if List[Index] == Value:
            Indexes.append(Index)
    return Indexes


def GetPossibleGuesses(PossibleGuesses, GuessHistory, ScoreHistory):
    """
    Creates a list of next PossibleGuesses based on previons Guesses and corresponding Scores.

    Args:
        PossibleGuesses: List. All Possible Guesses.
        GuessHistory: List. All previous Guesses
        ScoreHistory: List. All previous Scores
    
    Returns: List. Possible next guesses
    """
    for Index in range(len(GuessHistory)):
        PossibleGuesses = FilterGuesses(PossibleGuesses, GuessHistory[Index], ScoreHistory[Index])
    return PossibleGuesses


def SimpleAlogrithm(PossibleGuesses, GuessHistory, ScoreHistory):
    """
    Simple Algorithm:
    picks a random guess from all possible guesses.

    Args:
        PossibleGuesses: List. All possible Guesses
        GuessHistory: List. All previous Guesses
        ScoreHistory: List. All previous Scores
    
    Returns: String. A Guess
    """
    if ScoreHistory != []:
        PossibleGuesses = GetPossibleGuesses(PossibleGuesses, GuessHistory, ScoreHistory)
    Guess = PickGuess(PossibleGuesses, GuessHistory)
    return Guess


def PickGuess(PossibleGuesses, GuessHistory):
    """
    Picks a random guess from next possible guesses. And makes sure this guess hasn't already been tried.

    Args:
        PossibleGuesses: List. All Possible Guesses
        GuessHistory: List. All previous Guesses.
    
    Returns: String. Next Guess.
    """
    while True:
        Guess = random.choice(PossibleGuesses)
        if Guess not in GuessHistory:
            break
    return Guess


def PossibleCombinations(Colors=['A', 'B', 'C', 'D', 'E', 'F'], Positions=4, Text='', List=[]):
    """
    Generates a list with all possible combinations of codes.

    Args:
        Colors: List. Possible colors
        Positions: Integer. Length of the code.
        Text: String. Contains a single Possible Code.
        List: List. Contains all possible Guesses

    Returns: List. All possible combinations.
    """
    Positions = Positions - 1
    for i in Colors:
        Current = Text
        Current = Current + i
        if Positions > 0:
            List = PossibleCombinations(Colors, Positions, Current, List)
        else:
            List.append(Current)
    return List


def UserFeedback(LengthCode):
    """
    Lets the player give Feedback to Computer Guesses.

    Args:
        LengthCode: Integer. Length of the Code.
    
    Returns: List. Score given by the player
    """
    Colors = ['A', 'B', 'C', 'D', 'E', 'F']
    BadFeedback = True
    while BadFeedback:
        try:
            BlackPin = int(input('Geef aantal kleuren op juiste plek: '))
            if BlackPin == LengthCode:
                return [BlackPin,0]
            WhitePin = int(input('Geef aantal kleuren op verkeerde plek: '))
            if not BlackPin + WhitePin > LengthCode:
                Feedback = [BlackPin, WhitePin]
                BadFeedback = False
        except ValueError:
            pass
    return Feedback


def Start():
    """
    Start of the program, provides a menu for easy navigation.
    """
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
            try:
                Ammount = int(input("Enter the ammount of runs: "))
                StartDebug(Ammount)
            except ValueError:
                print('Invalid input')
        else:
            print('Invalid input')


def StartDebug(ammount):
    Simple = []
    Worst = []
    Own = []
    for i in range(ammount+1):
        print(i)
        Simple.append(Debug(Simple=True))
        Worst.append(Debug(Worst=True))
        Own.append(Debug(Own=True))

    print('\nSimple:\nMin :'+str(min(Simple))+'\nMax: '+str(max(Simple))+'\nAvg: '+str(round(sum(Simple)/len(Simple),2))+'\n')
    print('\nWorst:\nMin :'+str(min(Worst))+'\nMax: '+str(max(Worst))+'\nAvg: '+str(round(sum(Worst)/len(Worst),2))+'\n')
    print('\nOwn:\nMin :'+str(min(Own))+'\nMax: '+str(max(Own))+'\nAvg: '+str(round(sum(Own)/len(Own),2))+'\n')


def WorstCaseAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory):
    """
    Worst Case Algorithm:
    Checks the possible results for current possible guesses.
    Picks the guess that gives the shortest worst case scenario (length of PossibleGuesses).

    Args:
        PossibleGuesses: List. All possible Guesses
        GuessHistory: List. All previous Guesses
        ScoreHistory: List. All previous Scores
    
    Returns: String. A Guess
    """
    if ScoreHistory != []:
        PossibleGuesses = GetPossibleGuesses(PossibleGuesses, GuessHistory, ScoreHistory)
    Matrix = GenerateMatrix(PossibleGuesses)
    OptimalGuesses = FilterMatrix(PossibleGuesses, Matrix)
    Guess = PickGuess(OptimalGuesses, GuessHistory)
    return Guess


def OwnAlgorithm(PossibleGuesses, GuessHistory, ScoreHistory):
    """
    Own Algorithm:
    Modified Worst Case Algorithm.
    Ignores all Scores with 0 except the ones that equals the codelength.

    The idea behind this algorithm is that, when playing mastermind you want to get the most ammount of information in the least ammount guesses,
    guesses with a possible score containing a 0 are less usefull than scores that don't. So these are ignored.

    Args:
        PossibleGuesses: List. All possible Guesses
        GuessHistory: List. All previous Guesses
        ScoreHistory: List. All previous Scores
    
    Returns: String. A Guess
    """
    if ScoreHistory != []:
        PossibleGuesses = GetPossibleGuesses(PossibleGuesses, GuessHistory, ScoreHistory)
    Matrix = GenerateMatrix(PossibleGuesses)
    OptimalGuesses = FilterMatrix(PossibleGuesses, Matrix, True)
    Guess = PickGuess(OptimalGuesses, GuessHistory)
    return Guess
    

Start()







