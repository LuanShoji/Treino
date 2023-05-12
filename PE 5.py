y = 1
z = 20
while z != 0:
    for c in range(1, 21, 1):
        if y % c == 0:
            z -= 1
        else:
            y += 1
            print(y)

'''Resposta 232792560'''


