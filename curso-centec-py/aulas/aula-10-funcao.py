def somar(a, b):
    resultado = a + b


    return resultado


def fatorial(numero):
    resultado = numero


    for valor in range(numero - 1, 0, -1):
        resultado = resultado * valor
        
    return resultado


resultado = somar(3, 6)
print(resultado)


resultado = fatorial(5)
print(resultado)




