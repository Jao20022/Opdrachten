def functie():
    Dictionary = {}
    while True:
        naam = input("Volgende Naam: ")
        if naam == '':
            break
        if naam not in Dictionary.keys():
            Dictionary[naam] = 1
        else:
            Dictionary[naam] += 1
    for naam, keren in Dictionary.items():
        if keren > 1:
            print("Er zijn", keren, "studenten met de naam", naam)
        elif keren == 1:
            print("Er is 1 student met de naam", naam)
        else:
            print("Er is iets fout geegaan")

functie()