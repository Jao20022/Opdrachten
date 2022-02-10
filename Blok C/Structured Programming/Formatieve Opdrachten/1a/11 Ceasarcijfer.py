def Ceasarcijfer(String, Rotation):
    NewString = str()
    for i in String:
        Upper = None
        Lower = None
        Unicode = ord(i)
        if  65 <= Unicode <= 90:
            # Capital
            Upper = 90
            Lower = 65
        if  97 <= Unicode <= 122:
            # Lower
            Upper = 122
            Lower = 97
        if  48 <= Unicode <= 57: 
            # Digit
            Upper = 57
            Lower = 48
        if not Upper is None:
            Unicode = UnicodeConversion(Upper,Lower, Unicode, Rotation)
        NewString = NewString +chr(Unicode)
    return NewString
def UnicodeConversion(Upper,Lower,Unicode, Rotation):
    Unicode = Unicode + Rotation
    if Unicode > Upper:
        Unicode = Unicode - (Upper - Lower)
    return Unicode




String = input('Vul een zin in: ')
Rotation = int(input('Geef een rotatie: '))

print(Ceasarcijfer(String, Rotation))