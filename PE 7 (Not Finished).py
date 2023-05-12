'''p = [2]
z = 3
while len(p) != 6:
    for x in p:
        if z % x != 0:
            p.insert(0, z)
            z += 1
print(p)
print("FIM")'''
p = [2, 4, 6, 8, 3]
c = 24
z = 0
for x in p:
    if c % x == 0:
        c += 0
        x = c
    else:
        c += 1
if c == z:
    p.insert(0, c)
print(p)