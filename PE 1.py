s = 0
for p in range(0, 1000, 1):
    if p % 3 == 0 or p % 5 == 0:
        s += p
print(s)