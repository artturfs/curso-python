# Q.6 Calcular Fatorial

# entrada
numero = input('Digite o número para calcular o fatorial: ')
numero = int(numero)

# processamento
resultado = numero

for valor in range(numero - 1, 0, -1):
    resultado = resultado * valor

# saída
print('Resultado:', resultado)
