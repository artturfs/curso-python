

lista = ['davi', 'anderson', 'joão', 'flavin', 'mateus']


print(lista)


print( lista[2] )


dicionario = {
    'primeiro': 'davi',
    'segundo': 'anderson',
    'terceiro': 'joão',
    'quarto': 'larissa'
}


lista_nomes = ['davi', 'anderson', 'joão']
lista_idades = [29, 39, 18]


cadastro_pessoa1 = {
    'nome': 'Davi',
    'idade': 29,
    'peso': 82,
    'altura': 1.72
}


cadastro_pessoa2 = {
    'nome': 'Anderson',
    'idade': 39,
    'peso': 75,
    'altura': 1.80
}


lista = [9, 32, -8, 64, 18]


lista = [3.14, 6.0, 24.3, -16.8]


lista = [
    {
        'nome': 'Davi',
        'idade': 29
    },
    {
        'nome': 'Anderson',
        'idade': 39
    },
    {
        'nome': 'João',
        'idade': 18
    },
    {
        'nome': 'Larissa',
        'idade': 18
    },
    {
        'nome': 'Aerofólio Voador',
        'idade': 18
    }
]


cadastro_pessoa1 = {
    'nome': 'Davi',
    'idade': 29,
    'peso': 82,
    'altura': 1.72,
    'veiculo': {
        'marca': 'honda',
        'modelo': 'fan',
        'cc': 150
    },
    'cursos_ministrados': [
        'programação web',
        'python',
        'administração de servidores',
        'planejamento de carreira',
        'banco de dados'
    ]
}


print(cadastro_pessoa1)


print(cadastro_pessoa1['peso'])


cadastro_pessoa1['peso'] = 83


print(cadastro_pessoa1)


print(cadastro_pessoa1['veiculo'])


print(cadastro_pessoa1['veiculo']['cc'])


cadastro_pessoa1['veiculo']['cc'] = 160


print(cadastro_pessoa1['veiculo'])


print(cadastro_pessoa1['cursos_ministrados'])


print(cadastro_pessoa1['cursos_ministrados'][4])


cadastro_pessoa1['cursos_ministrados'].append('protocolos')


print('pessoa:')
print(cadastro_pessoa1)


# 'a' -> 'A'
# 'b' -> 'B'
# 'c' -> 'C'
# 'd' -> 'D'
alfabeto = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D'
}
