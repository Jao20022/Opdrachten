import json

# gebruik hier een herhalingslus:

while True:
    try:
        with open('pe_10_2_inloggers.json', 'r') as json_file:
            wam = json.load(json_file)
    except json.decoder.JSONDecodeError:
        wam = []
    naam = input("Wat is je achternaam? ")
    if naam == "einde":
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    wam.append({"naam" : naam, "voorletters" : voorl, "geb_datum" : gbdatum, "e-mail" : email})
    with open('pe_10_2_inloggers.json', 'w') as json_file:
        json.dump(wam, json_file, indent=4)

    # Maak een dictionary van de gegevens van deze gebruiker. Zie ook het voorbeeldbestand onderaan de pagina.
    # wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file.

