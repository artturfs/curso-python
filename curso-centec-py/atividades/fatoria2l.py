# Q.6 Calcular Fatorial

# entrada
numero = input('Digite o número para calcular o fatorial: ')
numero = int(numero)

# processamento e saída
print(numero, '! = ', sep = '', end = '')

resultado = 1

for valor in range(numero, 0, -1):
    print(valor, end = '')
    if valor > 1:
        print(' x ', end = '')

    resultado = resultado * valor

print(' =', resultado)