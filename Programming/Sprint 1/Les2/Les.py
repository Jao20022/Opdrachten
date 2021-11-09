lst = [50, 20000, 45693, 3253245, 324]

lst.append(160.00)
print(lst)

print(lst.count(160.00))

minimum = min(lst)
print(minimum)

print(lst.index(minimum))
lst.remove(minimum)
print(lst)

lst.sort()
print(lst)



uurloon = input()
print(uurloon)