Bruin = {'Boxtel', 'Best', 'Eindhoven', 'Helmond \'t Hout', 'Helmond Brouwhuis', 'Deurne'}
Groen = {'Boxtel', 'Best', 'Eindhoven', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

# 1
print(Bruin.intersection(Groen))
# 2
print(Bruin.difference(Groen))
# 3
totaal = Bruin.union(Groen)
print(totaal)
