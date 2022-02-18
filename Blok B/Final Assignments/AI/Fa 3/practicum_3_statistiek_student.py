#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 3: statistiek

(c) 2019 Hogeschool Utrecht,
Bart van Eijkelenburg en
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Werk onderstaande functies uit. Elke functie krijgt een niet-lege en
ongesorteerde lijst *lst* met gehele getallen (int) als argument.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
from ast import expr_context
from operator import indexOf
from re import L
from statistics import variance


naam = "Just Oudheusden"
klas = "B"
studentnummer = 1815037


def mean(lst):
    # berekent het gemiddelde en retourneert deze
    average = sum(lst)/len(lst)
    """
    Bepaal het gemiddelde van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het gemiddelde van de gegeven getallen.
    """
    return average


def rnge(lst):
    # Geeft verschil tussen de hoogste en laagste waarde uit lsts
    """
    Bepaal het bereik van een lijst getallen.
    
    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        int: Het bereik van de gegeven getallen.
    """
    range = max(lst)-min(lst)
    return range


def median(lst):
    # sorteert de lijst en retourneert de middelste waarde
    # als de lengte van de lijst even is. Wordt het gemiddelde van de middelste twee waardes geretourneert
    lst.sort()
    if len(lst) % 2 == 0:
        M = (lst[(len(lst)//2)-1] + lst[len(lst)//2])/2
    else:
        M = float(lst[len(lst)//2])
    """
    Bepaal de mediaan van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De mediaan van de gegeven getallen.
    """
    return M


def q1(lst):
    # sorteert de lijst en geeft de mediaan van de eerste helft
    # als de lijst oneven is wordt de middelste waarde uit de lijst gehaalt
    lst.sort()
    if not len(lst) % 2 == 0:
       lst.pop(len(lst)//2)
    Q1 = median(lst[:int(len(lst)/2)])
    """
    Bepaal het eerste kwartiel Q1 van een lijst getallen.

    Hint: maak gebruik van `median()`

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het eerste kwartiel Q1 van de gegeven getallen.
    """
    return Q1


def q3(lst):
    # sorteert de lijst en geeft de mediaan van de tweede helft
    # als de lijst oneven is wordt de middelste waarde uit de lijst gehaalt
    lst.sort()
    if not len(lst) % 2 == 0:
       lst.pop(len(lst)//2)
    Q3 = median(lst[int(len(lst)/2):])
    """
    Bepaal het derde kwartiel Q3 van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het derde kwartiel Q3 van de gegeven getallen.
    """
    return Q3


def var(lst):
    # berekent het gemiddelde van lst
    # berekent voor elke waarde in de lijst het verschil met de gemiddelde
    # neemt het kwadraat van deze waardes en voegt deze toe aan 'nieuwe_waarde'
    # berekent de variantie door het gemiddelde van 'nieuwe_waarde' te berekenen
    gemiddelde = sum(lst)/len(lst)
    nieuwe_waarde =[]
    for i in lst:
        gemiddelde_i = i - gemiddelde
        nieuwe_waarde.append(gemiddelde_i**2)
    variantie = sum(nieuwe_waarde)/len(lst)
    
    """
    Bepaal de variantie van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De variantie van de gegeven getallen.
    """
    return variantie


def std(lst):
    # berekent het gemiddelde van lst
    # berekent voor elke waarde in de lijst het verschil met de gemiddelde en voegt deze toe aan 'di'
    # berekent het kwadraat van deze waardes
    # berekent de gemiddelde van 'di' en slaat deze of als 'Kgem'
    # berekent de 'standaarddeviatie' door de wortel van 'Kgem' te nemen
    Xgem = sum(lst)/len(lst)
    di =[]
    for i in lst:
        di.append(i-Xgem)
    for j in range(len(di)):
        di[j] = di[j]**2
    Kgem = sum(di)/len(di)
    standaarddeviatie = Kgem**(1/2)
    """
    Bepaal de standaardafwijking van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De standaardafwijking van de gegeven getallen.
    """
    return standaarddeviatie


def freq(lst):
    # probeert eerst alle waardes aan de dictionary 'freqs' toe te voegen
    # geeft deze keys de waardes van het aantal dat die key voorkomt in de lijst.

    freqs = dict()
    for i in lst:
        freqs.update({i:''})
    for j in freqs:
        freqs[j] = lst.count(j)
    
    """
    Bepaal de frequenties van alle getallen in een lijst.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        dict: Een dictionary met als 'key' de waardes die voorkomen in de lijst
            en als 'value' het aantal voorkomens (de frequentie) van die waarde.

    Examples:
        >> freq([0, 0, 4, 7, 7])
        {0: 2, 4: 1, 7: 2}

        >> freq([1, 1, 2, 3, 2, 1])
        {1: 3, 2: 2, 3: 1}
    """
    
    return freqs


def modes(lst):
    # geeft 'freqs' het resultaat van functie freqs
    # voegt alle keys toe aan de lijst 'keys'
    # sorteert de lijst 'keys'
    # voegt de aantallen dat de keys voorkomen toe aan de lijst aantallen
    # haalt de hoogste waarde uit de lijst 'aantal' op en slaat deze op in 'Hoog'
    # voegt alle 'keys' met het aantal 'Hoog' toe aan de lijst 'modi'
    modi = []
    freqs = freq(lst)
    keys = []
    aantal = []
    for x in freqs.keys():
        keys.append(x)
    keys.sort()
    for i in keys:
        aantal.append(freqs[i])
    Hoog = max(aantal)
    for j in range(len(aantal)):
        if aantal[j] == Hoog:
            modi.append(keys[j])
    return modi

    

    """
    Bepaal alle modi van een lijst getallen.

    Hint: maak gebruik van `freq()`.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        list: Een gesorteerde lijst van de modi van de gegeven getallen.

    Examples:
        >> modes([0, 0, 4, 7, 7])
        [0, 7]

        >> modes([1, 1, 2, 3, 2, 1])
        [1]
    """
    
    return sorted(modi)


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_mean():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 3.0)
    ]

    for case in testcases:
        __my_assert_args(mean, case[0], case[1])


def test_mean_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(mean, (lst_test,), statistics.mean(lst_test), False)


def test_rnge():
    testcases = [
        (([4, 2, 5, 8, 6],), 6),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 5)
    ]

    for case in testcases:
        __my_assert_args(rnge, case[0], case[1])


def test_median():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 4, 6, 4, 2],), 3.5),
        (([1, 3, 4, 6, 2, 4, 2],), 3.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.5)
    ]

    for case in testcases:
        __my_assert_args(median, case[0], case[1])


def test_median_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(median, (lst_test,), statistics.median(lst_test), False)


def test_q1():
    testcases = [
        (([4, 2, 5, 8, 6],), 3.0),
        (([1, 3, 4, 6, 4, 2],), 2.0),
        (([1, 3, 5, 6, 1, 4, 2],), 1.0),
        (([5, 7, 4, 4, 6, 2, 8],), 4.0),
        (([0, 5, 5, 6, 7, 7, 12],), 5.0),
        (([1, 3, 3, 5, 6, 2, 4, 1],), 1.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 7.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 5.0)

    ]

    for case in testcases:
        __my_assert_args(q1, case[0], case[1])


def test_q3():
    testcases = [
        (([4, 2, 5, 8, 6],), 7.0),
        (([1, 3, 4, 6, 4, 2],), 4.0),
        (([1, 3, 5, 6, 2, 4, 1],), 5.0),
        (([5, 7, 4, 4, 6, 2, 8],), 7.0),
        (([0, 5, 5, 6, 7, 7, 12],), 7.0),
        (([1, 3, 3, 5, 6, 2, 4, 1],), 4.5),
        (([1, 3, 3, 5, 6, 2, 4, 1],), 4.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 16.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 18.0)

    ]

    for case in testcases:
        __my_assert_args(q3, case[0], case[1])


def test_var():
    testcases = [
        (([4, 2, 5, 8, 6],), 4.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.25)
    ]

    for case in testcases:
        __my_assert_args(var, case[0], case[1])


def test_var_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(var, (lst_test,), statistics.pvariance(lst_test), False)


def test_std():
    testcases = [
        (([4, 2, 5, 8, 6],), 2.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 1.5)
    ]

    for case in testcases:
        __my_assert_args(std, case[0], case[1])


def test_std_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(std, (lst_test,), statistics.pstdev(lst_test), False)


def test_freq():
    testcases = [
        (([4, 2, 5, 8, 6],), {2: 1, 4: 1, 5: 1, 6: 1, 8: 1}),
        (([1, 3, 4, 6, 4, 2],), {1: 1, 2: 1, 3: 1, 4: 2, 6: 1}),
        (([1, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        (([1, 3, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 2, 4: 1, 5: 1, 6: 1})
    ]

    for case in testcases:
        __my_assert_args(freq, case[0], case[1])


def test_modes():
    testcases = [
        (([4, 2, 5, 8, 6],), [2, 4, 5, 6, 8]),
        (([1, 3, 4, 6, 4, 2],), [4]),
        (([1, 3, 4, 6, 2, 4, 2],), [2, 4]),
        (([1, 3, 2, 4, 6, 2, 4, 2],), [2])
    ]

    for case in testcases:
        __my_assert_args(modes, case[0], case[1])


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_mean()
        test_mean_simulated()
        print("Je functie mean(lst) werkt goed!")

        test_rnge()
        print("Je functie rnge(lst) werkt goed!")

        test_median()
        test_median_simulated()
        print("Je functie median(lst) werkt goed!")

        test_q1()
        print("Je functie q1(lst) werkt goed!")

        test_q3()
        print("Je functie q3(lst) werkt goed!")

        test_var()
        test_var_simulated()
        print("Je functie var(lst) werkt goed!")

        test_std()
        test_std_simulated()
        print("Je functie std(lst) werkt goed!")

        test_freq()
        print("Je functie freq(lst) werkt goed!")

        test_modes()
        print("Je functie modes(lst) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

        def hist(freqs):
            v_min = min(freqs.keys())
            v_max = max(freqs.keys())

            histo = str()
            for i in range(v_min, v_max + 1):
                histo += "{:5d} ".format(i)
                if i in freqs.keys():
                    histo += "█" * freqs[i]
                histo += '\n'

            return histo

        print("\x1b[0m")
        s = input("Geef een reeks van gehele getallen (gescheiden door een spatie): ")
        userlst = [int(c) for c in s.split()]

        print("\nHet gemiddelde is {:.2f}".format(mean(userlst)))
        print("De modi zijn {}".format(modes(userlst)))
        print("De mediaan is {:.2f}".format(median(userlst)))
        print("Q1 is {:.2f}".format(q1(userlst)))
        print("Q3 is {:.2f}".format(q3(userlst)))

        print("Het bereik is {}".format(rnge(userlst)))
        print("De variantie is {:.2f}".format(var(userlst)))
        print("De standaardafwijking is {:.2f}".format(std(userlst)))

        print("\nHistogram (gekanteld):\n\n" + hist(freq(userlst)))

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
