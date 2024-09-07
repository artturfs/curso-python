

# penultimo: 0
# ultimo: 1


# proximo = penultimo + ultimo
# penultimo = ultimo
# ultimo = proximo


# 0 1


# entrada
n_termos = int(input('Digite quantos termos: '))


# processamento e saída
penultimo = 0
ultimo = 1


print(penultimo, ultimo, end = ' ')


for x in range(n_termos - 2):
    proximo = penultimo + ultimo
    print(proximo, end = ' ')


    penultimo = ultimo
    ultimo = proximo
