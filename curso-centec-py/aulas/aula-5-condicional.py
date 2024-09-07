idade = input('digite uma idade: ')
idade = int(idade)

if idade >= 100:
    print('já papocou')
elif idade >= 65:
    print('é aposentado')
elif idade >= 18:
    print('é maior')
else:
    print('é menor')