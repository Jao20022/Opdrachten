def rng(plaatshouder):
    return max(plaatshouder) - min(plaatshouder)


lijst = [2345, 342 - 5234, 5234, 5234 - 52, 345 - 2, 345234]

print(rng(lijst))
