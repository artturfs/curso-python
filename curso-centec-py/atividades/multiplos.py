x = int(input('Diga os multiplos de: '))
resultado = int(input('Diga até o limite: '))
str = 'Os multiplos são: '
print(str)

for Y in range (1, resultado + 1):
    multiplos = Y
    multiplos *= x
    print(x, '*', Y, '=', multiplos)