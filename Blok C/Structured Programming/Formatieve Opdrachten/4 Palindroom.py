x = input('Geef een string: ')
y = ''
for i in range(len(x)-1,-1,-1):
    y = y+x[i]

print(x)
print(y)

if x == y:
    print(x, 'Is een palindroom')
else:
    print(x, 'Is niet een palindroom')