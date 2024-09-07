

# Q.37 Contar palavras com um determinado comprimento.

# entrada
texto = input('Digite seu texto: ')
comprimento = int(input('Digite o comprimento para contar: '))

# processamento
lista_palavras = texto.split()

contador = 0

for palavra in lista_palavras:
    if len(palavra) == comprimento:
        contador += 1

# saída
print('Quantidade de palavras:', contador)
