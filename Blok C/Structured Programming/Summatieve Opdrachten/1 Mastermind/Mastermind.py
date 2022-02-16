Lijst = []
Kleuren = ['A','B','C','D','E','F']
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
    

def Mastermind(CorrectCombination,Guess):
    Feedback = [0,0]
    for i in range(CorrectCombination-1):
        if CorrectCombination[i] == Guess[i]:
            Feedback[0] = Feedback[0] +1
        elif(Guess[i] in CorrectCombination and )
    return Feedback