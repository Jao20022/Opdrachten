# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#
## A
# print(lst[:4])
#
## B
# print(lst[3:6])
#
## C
# print(lst[3:4])
#
## D
# print(lst[-3:-1])
#
## E
# print(lst[3:])
#
## F
# print(lst[-3:])
#

#
# events = '9/13 2:30 PM\n9/14 11:15 AM\n9/14 1:00 PM\n9/15 9:00 AM'
# print(events, '\n')
#
## A
# print(events.count('9/14'))
#
## B
# print(events.find('9/14'))
#
## C
# print(events.find('9/15'))
#
## D
# ev_914 = events[13:40].strip().split('\n')
# print(ev_914)

# print(events.split('\n'))


# getal1 = 3.1239128039812903810293
# getal2 = 32.2342343424234
#
#
# resultaat = getal1 + getal2
#
# bericht1 = "Getal {} + {} = {:.2f}".format(getal1, getal2, resultaat)
# bericht2 = f"Getal {getal1} + {getal2} = {resultaat:.2f}"
#
#
#
# print(bericht1)
# print(bericht2)

import math
file = open('onzin.txt', 'w')
file.write(str(math.pi))



print(math.pi)