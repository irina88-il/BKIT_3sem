a = [1,2,3]
#b = [(1,1),(2,4),(3,9)]

b1 = [(i, i**2) for i in a]
print(b1)

b2 = list(zip(a,[i**2 for i in a]))
print(b2)

b3 = list(list(map(lambda i:(i, i**2),a)))
print(b3)