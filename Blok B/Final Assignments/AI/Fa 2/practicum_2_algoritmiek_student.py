#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 2: algoritmiek

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
from operator import indexOf


naam = "Just Oudheusden"
klas = "B"
studentnummer = 1815037

"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die deze
        lijst aanneemt bij álle tussenstappen bij toepassing van
        bovenstaand sorteeralgoritme.
"""
        # TODO: [[4,3,1,2],[3,4,1,2],[3,1,4,2],[1,3,4,2],[1,3,2,4],[1,2,3,4]
''''
[ 4, 3, 1, 2 ]
        1. vergelijk 0 met 1
        2. 1 is groter dan 0 dus verwissel ze
[3, 4, 1, 2]
        4. vergelijk 0 met 1
        5. 0 is niet groter dan 1 dus er gebeurt niks
        6. vergelijk 1 met 2
        7. 1 is groter dan 2 dus verwissel ze
[3, 1, 4, 2]
        8. vergelijk 0 met 1
        9. 0 is groter dan 1 dus verwissel ze
[1, 3, 4, 2]
        10. vergelijk 0 met 1
        11. 0 is niet groter dan 1 dus er gebeurt niks
        12. vergelijk 1 met 2
        13. 1 is niet groter dan 2 dus er gerbeurt niks
        14. vergelijk 2 met 3
        15. 2 is groter dan 3 dus verwissel ze
[1, 3, 2, 4]
        16. vergelijk 0 met 1
        17. 0 is niet groter dan 1 dus er gebeurt niks
        18. vergelijk 1 met 2
        19. 1 is groter dan 2 dus verwissel ze
[1, 2, 3, 4]
        20. vergelijk 0 met 1
        21. 0 is niet groter dan 1 dus er gebeurt niks
        20. vergelijk 1 met 2
        21. 1 is niet groter dan 2 dus er gebeurt niks
        20. vergelijk 2 met 3
        21. 2 is niet groter dan 3 dus er gebeurt niks
        22. klaar
'''

"""

    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie
        hieronder genaamd my_sort(lst).

    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke
            volgorde van de waarden in de lijst is het sorteeralgoritme
            het snelste klaar (best-case scenario)?
            Hoeveel vergelijkingen (zoals beschreven in stap 1. van de
            pseudocode) zijn nodig geweest?
"""
            # TODO: [[1,2,3] het algoritme is in 2 stappen klaar]
"""


        -   Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het minst snel klaar (worst-case scenario)?
            Hoeveel vergelijkingen zijn nodig geweest?
"""
            # TODO: [[3,2,1] het algoritme is in 6 stappen klaar]
"""


        -   Stel je hebt een lijst met de waarden 1 tot en met 4.
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
            # TODO: [geef hier je antwoord]
            # TODO: Best Case: [1,2,3,4] het algoritme is in 3 stappen klaar
            # TODO: Worst Case: [4,3,2,1] het algoritme is in 12 stappen klaar
"""


        -   Stel je hebt een lijst met de waarden 1 tot en met n
            (je weet nu dus niet precies hoeveel waarden er in de lijst
            zitten, het zijn er 'n').
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
            # TODO: [geef hier je antwoord]
            # TODO: Best case = [1,2,...,n] er zijn n-1 stappen nodig
            # TODO: Worst case = [n,...,2,1] er zijn (n-1)*n stappen nodig
"""
"""


def my_sort(lst):
    # kopie van lst wordt gemaakt
    lst_sorted = lst.copy()
    i = 0
    # vergelijkt i met de volgende in de reeks, als de volgorde niet klopt worden ze verwisselt en gaat i terug naar 0
    # anders wordt i met 1 verhoogt en wordt het herhaalt
    while i < len(lst_sorted) -1:
        if lst_sorted[i] > lst_sorted[i + 1]:
            lst_sorted[i],lst_sorted[i+1] = lst_sorted[i+1], lst_sorted[i]
            i = 0
        else:
            i += 1


    """
    Sorteer gegeven lijst volgens het algoritme zoals beschreven in de pseudocode.

    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    return lst_sorted


def linear_search_recursive(lst, target):
    # Controleert voor elke index of deze overeenkomt met de target.
    # Als de loop geen True retourneerd wordt False geretourneerd
    i = 0
    while True:
        if lst[i] == target:
            return True
        else:
            i = i+1
            if i == len(lst):
                return False
            
        
    """
    Zoek een element in de gegeven lijst door middel van recursief lineair zoeken.

    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
    """
 


def binary_search_recursive(lst, target):
    # maakt een kopie van lst
    # neemt de middelste item als gok
    # als gok gelijk is aan target retourneert True
    # als lengte van lst 1 is retourneert False
    # a;s de target kleiner is dan de gok wordt lst_copy verkort tot voor de gok
    # als target groter is dan de gok wordt lst_copy verkort tot vanaf de gok
    lst_copy = lst.copy()
    while True:
        guess = lst_copy[len(lst_copy)//2]
        if guess == target:
            return True
        elif len(lst_copy) == 1:
            return False
        elif guess < target:
            lst_copy = lst_copy[lst_copy.index(guess):]
        elif guess > target:
            lst_copy = lst_copy[:len(lst_copy)-lst_copy.index(guess)]

    """
    Zoek een element in de gegeven lijst door middel van recursief binair zoeken.

    Je mag ervan uit gaan dat de gegeven lijst al gesorteerd is.
    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
    """



"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_my_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def test_linear_search_recursive():
    for _ in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = linear_search_recursive(lst_test, target)
        assert lst_copy == lst_test, "Fout: linear_search_recursive(lst, target) verandert de inhoud van lijst lst"
        assert outcome == found, \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"


def test_binary_search_recursive():
    for _ in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = binary_search_recursive(lst_test, target)
        assert outcome == found, \
            f"Fout: binary_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"
        assert lst_copy == lst_test, "Fout: binary_search_recursive(lst, target) verandert de inhoud van lijst lst"


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        print("Je functie linear_search_recursive() werkt goed!")

        test_binary_search_recursive()
        print("Je functie binary_search_recursive() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()
