lijst = ['a','b','c']
def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.insert(0, 'd')
    letterlijst.insert(1, 'e')
    letterlijst.insert(2, 'f')




print(lijst)
wijzig(lijst)
print(lijst)

# A omdat je dan een nieuwe variabele binnen de functie maakt
# Nee, de clear functie werkt niet op strings
# Lists zijn mutiple op manieren dat andere types dat niet zijn