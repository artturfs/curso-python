

# Q.28 Calcular área e perímetro do retângulo.

# função: calcular área de retângulo
def area(a, l):
    return a * l

# função: calcular o perímetro de retângulo
def perimetro(a, l):
    return 2 * (a + l)

# entrada
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

# processamento
resul_area = area(altura, largura)
resul_perimetro = perimetro(altura, largura)

# saída
print('Área:', resul_area)
print('Perímetro:', resul_perimetro)