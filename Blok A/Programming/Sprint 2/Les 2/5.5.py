def kwadraten_som(grondgetallen):
    uitkomst = 0
    for i in grondgetallen:
        if i > 0:
            uitkomst += i**2

    return uitkomst



print(kwadraten_som([2,3,-5]))