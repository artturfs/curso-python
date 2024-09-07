lista_numeros = [9, 4, 7, 10, 12, 6]

# 0 - 5: 0, 1, 2, 3, 4, 5
# indice: 0
# pega valor pelo índice (cria transitividade)
for indice in range(6):
    valor = lista_numeros[indice]
    print(valor)

# pega valor diretamento do array
for valor in lista_numeros:
    print(valor)

#        01234...
texto = 'um texto qualquer'

for caractere in texto:
    print(caractere)

print('novas funções:')
print(texto[6])
print(texto[4:6])

print(texto[7::-1])
print(texto[::-1])
