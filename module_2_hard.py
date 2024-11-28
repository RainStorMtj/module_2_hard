n = int(input('В первом поле камень с числом (3-20): '))

def shifr(n):
    parol = ''
    for i in range(1, n):
        for j in range(1, n):
            if j <= i:
                continue
            elif n % (i + j) == 0:
                parol += str(i) + str(j)
    return parol
result = shifr(n)
print('Пароль: ', result)