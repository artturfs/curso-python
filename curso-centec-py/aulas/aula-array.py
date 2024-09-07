# INTEIRO: 1 2 3...
# FLOAT: 3.5 6.0
# STRING: 'textual'

# Índice:         0          1          2
lista_nomes = ['paulo', 'jefferson', 'mateus', 'pedro']

print(lista_nomes)

print( lista_nomes[2] )

lista_nomes[2] = 'anderson'

print(lista_nomes)

for indice in range(3): # 0 1 2
    print('indice:', indice)
    print( lista_nomes[indice] )

lista_nomes = [
    'pedro',
    'eduardo',
    'gabriel',
    'pedro',
    'lucy',
    'varlen',
    'mateus',
    'israel',
    'paulo',
    'pedro'
]

print(lista_nomes)
print( len(lista_nomes) )

lista_nomes.append('yghor')

print(lista_nomes)
print( len(lista_nomes) )

indice = lista_nomes.index('paulo')
print(indice)

lista_nomes.remove('pedro')
print(lista_nomes)