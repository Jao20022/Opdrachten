def sorteren(Lijst):
    GesorteerdeLijst = []
    while len(Lijst) > 0:
        Kleinste = 0
        for i in range(len(Lijst)):
            if Lijst[i] < Lijst[Kleinste]:
                Kleinste = i
        GesorteerdeLijst.append(Lijst.pop(Kleinste))
    return GesorteerdeLijst


