def GemiddeldeBerekenen(Lijst):
    Gemiddelde = sum(Lijst) / len(Lijst)
    return Gemiddelde

def Lijsten(Lijst):
    for i in range(len(Lijst)):
        Lijst[i] = GemiddeldeBerekenen(Lijst[i])
    return Lijst

