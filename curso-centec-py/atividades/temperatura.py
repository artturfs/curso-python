# Q.11 Conversor de Temperatura C - F e vice-versa

# entrada
print('Conversor de Temperatura')
print('1 - De °C para °F')
print('2 - De °F para °C')
opcao = input('Digite sua opção: ')

temperatura = input('Digite a temperatura: ')
temperatura = float(temperatura)

# processamento e saída
if opcao == '1':
    resultado = temperatura * 1.8 + 32
    print('A temperatura em F é:', resultado, '°F')
elif opcao == '2':
    resultado = (temperatura - 32) / 1.8
    print('A temperatura em C é:', resultado, '°C')
else:
    print('Opção inválida.')