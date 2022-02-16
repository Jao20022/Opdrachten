from sre_constants import SUCCESS
from tracemalloc import start
from turtle import clearscreen


Lijst = []
Colors = ['A','B','C','D','E','F']
Tekst = ''



def PossibleCombinations(Colors, Positions,Text, List):
    Positions = Positions - 1
    for i in Colors:
        Current = Text
        Current = Current + i
        if Positions > 0:
            List = PossibleCombinations(Colors, Positions,Current, List)
        else: List.append(Current)
    return List
    

def Feedback(CorrectCombinationStr,GuessStr):
    CorrectCombination = []
    Guess = []
    for Letter in CorrectCombinationStr:
        CorrectCombination.append(Letter)
    for Letter in GuessStr:
        Guess.append(Letter)
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

def Start():
    while True:
        print("""
        Menu:
        
        1. Codebreaker
        2. Codemaker
         """)
        UserInput = input('Select a choice: ')
        if UserInput == '1':
            Codebreaker()
        elif UserInput == '2':
            Codemaker()
        else:
            print('Invalid input')

def EnterCode():
    BadCode = True
    while BadCode:
        BadCode = False
        Code = input('Vul een code in met een lengte van 4.\nJe kun kiezen uit: A,B,C,D,E,F: ').upper()
        for i in Code:
            if not i in Colors or len(Code) != 4:
                BadCode = True
    return Code
def Codebreaker():
    print('Codebreaker')

def Codemaker():
    print('Codemaker')
    Code = EnterCode()
    while True:
        print('success')



Start()