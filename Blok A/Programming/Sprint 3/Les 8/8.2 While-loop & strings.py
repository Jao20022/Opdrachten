while True:
    text = input('Geef een string van vier letters: ')
    if len(text) == 4:
        break
    print(text, 'heeft', len(text), 'letters')
print('Inlezen van correcte string:', text, 'is geslaagd')
