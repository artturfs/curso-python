

# Q.3 Contar vogais em string


# entrada
texto = input('digite seu texto: ')


# processamento
contador = 0


for c in texto:
    if c in ['a', 'e', 'i', 'o', 'u']:
        contador += 1


# saída
print('Quant. de vogais:', contador)
