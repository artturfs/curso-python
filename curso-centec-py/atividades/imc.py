# entrada
peso = input('digite seu peso (kg): ')
altura = input('digite sua altura (metros): ')

peso = float(peso)
altura = float(altura)

# processamento
imc = peso / (altura ** 2)

# saída
print(f'Seu IMC é: {imc:.2f}')

if imc <= 18.4:
    print('Classificação: Magreza')

if imc >= 18.5 and imc <= 24.9:
    print('Classificação: Adequado')

if imc >= 25.0 and imc <= 29.9:
    print('Classificação: Pré-Obeso')

if imc >= 30.0:
    print('Classificação: Obesidade')
