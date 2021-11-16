# Lijst met het traject
Stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']


def Station_In_Traject(X,Stations): # Controleert of X in de lijst met stations voor komt
    for Station in Stations: # Checkt of X in Stations voor komt
        if X.lower() == Station.lower(): # vergelijkt X met een van de stations
            return Station # returned het station
    return -1 # Foutcode wanneer het station niet in de lijst voorkomt

def Inlezen_Beginstation(Stations): # Controleert eindstation
    while True: # Herhaalt tot een station ingevoerd is
        X = input('Wat is je beginstation?\n>> ') # Vraagt om beginstation
        Beginstation = Station_In_Traject(X, Stations) # Gebruikt de functie Station_In_Traject
        if Beginstation != -1: # Als er geen foutcode teruggegeven wordt, wordt Beginstation gereturned
            return Beginstation # returned beginstation

def Inlezen_Eindstation(Stations, Beginstation): # Controleert Eindstation)
    while True: # Herhaalt tot een goede input ingevoerd is
        X = input('Wat is je eindstation?\n>> ') # Vraagt de gebruiker om input
        Eindstation = Station_In_Traject(X, Stations) # Gebruikt de functie Station_In_Traject
        if Eindstation != -1: # Als er geen foutcode teruggegeven wordt gaat de functie naar de volgende if statement
            if Stations.index(Beginstation) < Stations.index(Eindstation): # controleert of het eindstation na het beginstation komt
                return Eindstation # returned eindstation
            else: # als eindstation voor beginstation komt
                print(f'Deze trein komt niet in {Eindstation}.')

def Omroepen_Reis(Stations, Beginstation, Eindstation): # print output
    IndexBeginstation = Stations.index(Beginstation)
    IndexEindstation = Stations.index(Eindstation)
    Afstand = IndexEindstation - IndexBeginstation
    for i in range(IndexBeginstation+1, IndexEindstation):
        s = f"- {Stations[i]}"
    Prijs = Afstand * 5
    return f"Het beginstation {Beginstation} is het {IndexBeginstation+1}e station in het traject.\n Het eindstation {Eindstation} is het {IndexEindstation+1}e station in het traject.\n De afstand bedraagt {Afstand} station(s)\nDe prijs van het kaartje is {Prijs} euro.\n\nJij stapt in de trein in: {Beginstation}\n{s}\nJij stapt uit in: {Eindstation}"


Beginstation = Inlezen_Beginstation(Stations)             # Voort de functies uit
Eindstation = Inlezen_Eindstation(Stations, Beginstation) # Voort de functies uit
print(Omroepen_Reis(Stations, Beginstation, Eindstation))        # Voort de functies uit
#beginstation = inlezen_beginstation(stations)
#eindstation = inlezen_eindstation(stations, beginstation)
#print(omroepen_reis(stations, beginstation, eindstation))
