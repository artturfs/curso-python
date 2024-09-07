entrada = input('digite sua idade: ')

idade = int(entrada)

# SE a idade for maior ou igual a 18 anos, ENTÃO:
#   é maior de idade
# CASO CONTRÁRIO (SENÃO)
#   é menor de idade

# >= <= > < == !=

if idade >= 18:
    print('é maior de idade')
else:
    print('é menor')


if idade > 65:
    print('é aposentada')
else:
    print('não é aposentada')


if idade == 65:
    print('é momento de aposentar')