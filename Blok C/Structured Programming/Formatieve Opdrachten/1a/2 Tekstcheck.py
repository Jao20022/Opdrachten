String_1 = input('Geef een string: ')
String_2 = input('Geef een string: ')

def Tekstcheck(String1, String2):
    for i in range(len(String1)):
        try:
            if String1[i] != String2[i]:
                return i
        except IndexError:
            return i


print('Het eerste verschil zit op index:', Tekstcheck(String_1,String_2))