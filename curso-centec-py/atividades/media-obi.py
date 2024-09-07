

# Q.20 Cálculo de média de lista de números segundo OBI
# Olimpíada Brasileira de Informática (Programação)


# '12 15 23 8'


quant = int(input()) # Quantidade de números
entrada = input() # Os números separados por espaço


lista = entrada.split() # Separa nos espaço e coloca em lista


somatorio = 0


for valor in lista:
    somatorio += float(valor)


print(somatorio / quant)
