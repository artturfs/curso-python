#                0   1  2  3   4  5  6  7  8  9 10 11
lista_numeros = [12, 8, 3, 9, -1, 9, 4, 6, 3, 9, 0, 8]

acumuladora = 0

for i in range(len(lista_numeros)):
    valor = lista_numeros[i]
    acumuladora = valor + acumuladora

print('Soma total: ', acumuladora)

# vias de regras, toda vez que eu quiser gerar os indices de uma lista, usar o len dentro do range