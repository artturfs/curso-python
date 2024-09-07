# A.6 Sistema de Gerenciamento de Funcionários


lista_funcionarios = []
novo_id = 1


# função: adicionar um novo funcionário
def adicionar_func():
    global novo_id # global serve para alterar a variável criada fora da função
    novo_func = {}


    novo_func['nome'] = input('\nDigite o nome: ')
    novo_func['id'] = novo_id
    novo_func['cargo'] = input('Digite o cargo: ')
    novo_func['salario'] = float(input('Digite o salário: '))


    lista_funcionarios.append(novo_func)
    novo_id += 1 # alterar o id para que o id do próx. novo seja diferente




# função: buscar funcionário pelo ID
def buscar_func():
    id = int(input('\nDigite o ID do funcionário para buscar: '))


    func_encontrado = 0


    for func in lista_funcionarios:
        if func['id'] == id:
            func_encontrado = func
            break
    
    if func_encontrado == 0:
        print('\nFuncionário não existe!\n')
    else:
        print('\nEncontrado:')
        print('Nome:', func_encontrado['nome'], end = ', ')
        print('ID:', func_encontrado['id'], end = ', ')
        print('Cargo:', func_encontrado['cargo'], end = ', ')
        print('Salário:', func_encontrado['salario'])




# função: deletar funcionário pelo ID
def deletar_func():
    id = int(input('\nDigite o ID do funcionário para deletar: '))


    func_encontrado = 0


    for func in lista_funcionarios:
        if func['id'] == id:
            func_encontrado = func
            break
    
    if func_encontrado == 0:
        print('\nFuncionário não existe!\n')
    else:
        lista_funcionarios.remove(func_encontrado)
        print('\nFuncionário deletado!\n')




# função: editar funcionário
def editar_func():
    id = int(input('\nDigite o ID do funcionário para editar: '))


    func_encontrado = 0


    for func in lista_funcionarios:
        if func['id'] == id:
            func_encontrado = func
            break


    if func_encontrado == 0:
        print('\nFuncionário não existe!\n')
    else:
        func_encontrado['nome'] = input('\nDigite o novo nome: ')
        func_encontrado['cargo'] = input('Digite o novo cargo: ')
        func_encontrado['salario'] = float(input('Digite o novo salário: '))




# função: listar todos os funcionários
def listar_func():
    print('\nLista de Funcionários:')


    for func in lista_funcionarios:
        print('Nome:', func['nome'], end = ', ')
        print('ID:', func['id'], end = ', ')
        print('Cargo:', func['cargo'], end = ', ')
        print('Salário:', func['salario'])




# menu
opcao = 0


while opcao != 6:
    print('\nGESTÃO DE FUNCIONÁRIOS\n')
    print('1. Adicionar funcionário')
    print('2. Buscar funcionário')
    print('3. Editar funcionário')
    print('4. Deletar funcionário')
    print('5. Listar todos os funcionários')
    print('6. Sair\n')
    opcao = int(input('Escolha uma opção: '))


    if opcao == 1:
        adicionar_func()
    elif opcao == 2:
        buscar_func()
    elif opcao == 3:
        editar_func()
    elif opcao == 4:
        deletar_func()
    elif opcao == 5:
        listar_func()


print('\nPROGRAMA FINALIZADO.\n')
