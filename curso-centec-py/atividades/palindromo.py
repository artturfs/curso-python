#Q.4 Verificar palíndromo

# entrada
texto = input('digite sua frase: ')

# processamento e saída
novo_texto = texto.replace(' ', '')
novo_texto = novo_texto.lower()

if novo_texto == novo_texto[::-1]:
    print('É palíndromo.')
else:
    print('NÃO é palíndromo.')