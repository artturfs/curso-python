

# Q.14 Somar dígitos de um número.


entrada = input('Digite um valor inteiro: ')
entrada = entrada.replace('-', '')


somatorio = 0


for digito in entrada:
    valor = int(digito)
    somatorio += valor


print('A soma é:', somatorio)
