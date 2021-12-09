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
naam = "Just Oudheusden"
klas = "B"
studentnummer = 5

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
    step_one = lst[0:2]
    if step_one[0] > step_one[-1]:
        step_one.reverse()
    step_two = lst[2:4]
    if step_two[0] > step_two[-1]:
        step_two.reverse()
    step_three = lst[4:6]
    if step_three[0] > step_three[-1]:
        step_three.reverse()
    lst_sorted = step_one + step_two + step_three
    print(step_one)
    print(step_two)
    print(step_three)
    print(lst_sorted)
    while True:
        step_four = lst_sorted[0:2]
        if step_four[0] > step_four[1]:
            step_four.reverse()
        step_five = lst_sorted[1:3]
        if step_five[0] > step_five[1]:
            step_five.reverse()
        step_six = lst_sorted[2:4]
        if step_six[0] > step_six[1]:
            step_six.reverse()
        step_seven = lst_sorted[3:5]
        if step_seven[0] > step_seven[1]:
            step_seven.reverse()
        step_eight = lst_sorted[4:6]
        if step_eight[0] > step_eight[1]:
            step_eight.reverse()
        step_nine = lst_sorted[5:7]
        if step_nine[0] > step_six[1]:
            step_six.reverse()
        lst_sorted = step_four + step_five + step_six
        if lst.sort() == lst_sorted:
            break
    return lst_sorted




def linear_search_recursive(lst, target):
    # Controleert voor elke index of deze overeenkomt met de target.
    # Als de loop geen True retourneerd wordt False geretourneerd
    for i in range(len(lst)):
        if lst[i] == target:
            return True
    """
    Zoek een element in de gegeven lijst door middel van recursief lineair zoeken.

    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
    """
    return False


def binary_search_recursive(lst, target):
    # Variable worden aangemaakt
    # minumum is eerste index van lst
    minimum = 0
    # maximum is de hoogste index uit lst
    maximum = len(lst) -1
    # mid is een integer
    mid = int
    while True:
    # het gemiddelde wordt van de min en max berekend en naar beneden afgerond
        mid = int(((minimum + maximum)/2) // 1)
    # Als minimum groter is dan maximum zit de target niet in de lijst en wordt False geretourneerd
        if minimum > maximum:
            return False
    # Als mid gelijk is aan de target wordt True geretourneerd
        elif lst[mid] == target:
            return True
    # Als mid kleiner is dan de target wordt minimum verhoogt naar mid + 1
        elif lst[mid] < target:
            minimum = mid +1
    # Anders wordt maximum verlaag naar mid -1
        else:
            maximum = mid -1
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
