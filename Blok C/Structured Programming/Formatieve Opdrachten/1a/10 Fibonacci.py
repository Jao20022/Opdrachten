def FibonaciRecursive(Prev, Res, Index, n):
    Current = Prev + Res
    Prev, Res = Res, Current
    Index = Index + 1
    if Index != n:
        Res = FibonaciRecursive(Prev, Res, Index, n)
    return(Res)


def Fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        Result = FibonaciRecursive(0,1,1,n)
        return Result

f = 9
print('f'+str(f), 'geeft:', str(Fibonaci(f)))