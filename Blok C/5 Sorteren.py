def sorteren(Lijst):
    GesorteerdeLijst = []
    while len(Lijst) > 0:
        Kleinste = 0
        for i in range(len(Lijst)):
            if Lijst[i] < Lijst[Kleinste]:
                Kleinste = i
        GesorteerdeLijst.append(Lijst.pop(Kleinste))
    return GesorteerdeLijst


x = [5,4,5,4,5,43,3,43,45,4,3,4,5,3,4,5,3,23,4,5,4,63,45,1,4]
print(sorteren(x))