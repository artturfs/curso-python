numero = int(input('Digite um valor para iniciar a tabuada? '))
print('Escolha a alternativa da operação:')
print('A) Soma')
print('B) Subtração')
print('C) Multiplicação')
print('D) Divisão')

alternativa = input()

if alternativa == 'a':
    for mult in range (1, 11, 1):
        calculo = numero + mult
        print(numero, '+', mult, '=', calculo)

elif alternativa == 'b':
    for mult in range (1, 11, 1):
        calculo = numero - mult
        print(numero, '-', mult, '=', calculo)

elif alternativa == 'c':
    for mult in range (1, 11, 1):
        calculo = numero * mult
        print(numero, '*', mult, '=', calculo)

elif alternativa == 'd':
    for mult in range (1, 11, 1):
        calculo = numero / mult
        print(numero, '/', mult, '=', calculo)

else:
    print('Aletrnativa invalida')