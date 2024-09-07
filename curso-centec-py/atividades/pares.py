#                0  1  2  3  4  5  6
lista_numeros = [7, 3, 9, 6, 2, 0, 5]

print('Pares:')

for indice in range( len(lista_numeros) ):
    valor = lista_numeros[indice]

    if valor % 2 == 0:
        print(valor)
