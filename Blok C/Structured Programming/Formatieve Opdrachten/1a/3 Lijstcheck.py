def count(Getal, Lijst):
    Aantal = 0
    for i in Lijst:
        if i == Getal:
            Aantal = Aantal+1
    return Aantal


def GrootsteVerschil(Lijst):
    Max = 0
    for i in range(len(Lijst)-1):
        Verschil = Lijst[i]- Lijst[i+1]
        if Verschil < 0:
            Verschil = Verschil * 1
        if Verschil > Max:
            Max = Verschil
    return Max

def Eisen(Lijst):
    Nullen = count(0, Lijst)
    Enen = count(1, Lijst)
    if Enen > Nullen and Nullen <= 12:
        return True
    else:
        return False
    



