pessoa = {
    'nome': 'Davi Magalhães',
    'idade': 29,
    'cpf': '123.456.789-01',
    'altura': 1.72,
    'veiculo': {
        'marca': 'honda',
        'modelo': 'civic',
        'ano': 2005
    }
}


print(pessoa)


print( pessoa['nome'] )


pessoa['nome'] = 'Davi'


print(pessoa)


print(pessoa['veiculo']['modelo'])


pessoa['veiculo']['modelo'] = 'fan 160'


print(pessoa['veiculo']['modelo'])


pessoa['peso'] = 81


print(pessoa)


chave = 'profissao'


pessoa[chave] = 'professor'


print(pessoa)


lista_pessoas = [
    {
        'nome': 'davi',
        'idade': 29
    },
    {
        'nome': 'paulo',
        'idade': 18
    },
    {
        'nome': 'larissa',
        'idade': 18
    }
]


print('lista:')
print(lista_pessoas)


print(lista_pessoas[0])


print(lista_pessoas[0]['nome'])


lista_pessoas[0]['nome'] = 'Davi Magalhães'


if 'nome' in pessoa:
    print('chave existe em pessoa')
else:
    print('NÃO existe em pessoa')
