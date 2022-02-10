def CyclischVerschuiven(ch,n):
    if n > 0:
        for i in range(n+1):
            x = ch[-1]
            ch = ch[:-1]
            ch = x + ch
    elif n < 0:
        n = n * -1
        for i in range(n-1):
            x = ch[0]
            ch = ch[1:]
            ch = ch + x
    return ch



print(CyclischVerschuiven('1011000',3))
print(CyclischVerschuiven('1011100',-4))
print(CyclischVerschuiven('1011100',0))