print('MENU - CALCULADORA')
print('A - Somar')
print('B - Subtrair')
print('C - Multiplicar')
print('D - Dividir')
opcao = input('Digite sua opção: ')

print('Opção escolhida foi:', opcao)

if opcao == 'a' or opcao == 'A':
    print('somar')
elif opcao == 'b' or opcao == 'B':
    print('subtrair')
elif opcao == 'c' or opcao == 'C':
    print('multiplicar')
elif opcao == 'd' or opcao == 'D':
    print('dividir')
else:
    print('Opção inválida.')