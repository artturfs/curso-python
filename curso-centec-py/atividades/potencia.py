# Q.22 Calcular Potência

# entrada
base = int(input('Digite a base:')) # 3
expoente = int(input('Digite o expoente: ')) # 5

# processamento
resultado = base

for x in range(expoente - 1):
    resultado = resultado * base

# saída
print('Resultado:', resultado)
