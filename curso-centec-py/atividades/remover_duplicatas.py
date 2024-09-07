

# Q.15 Remover elementos repetidos em lista.


# processamento
lista_numeros = [3, 8, 12, 4, 7, 8, 15, 12, -3, 25, 4, 79]


nova_lista = []


for valor in lista_numeros:
    if valor not in nova_lista:
        nova_lista.append(valor)


# saída
print('Antiga:', lista_numeros)
print('Nova:', nova_lista)
