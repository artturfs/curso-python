# Q.9 Contar palavras em string.


texto = input('Digite seu texto: ')


texto = texto.strip()


contador = 1


for c in texto:
    if c == ' ':
        contador += 1


print('Quant. de palavras:', contador)
