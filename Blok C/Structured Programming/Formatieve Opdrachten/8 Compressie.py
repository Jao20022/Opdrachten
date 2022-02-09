Input = 'Input.txt'

with open(Input) as Bestand:
    Tekst = Bestand.read()
    Tekst = Tekst.replace(' ', '')
    Tekst = Tekst.replace('\n', '')
    Tekst = Tekst.replace('\t', '')

Output = Input.replace('.txt', '_Compressed.txt')

with open(Output, 'w') as Output:
    Output.write(Tekst)

