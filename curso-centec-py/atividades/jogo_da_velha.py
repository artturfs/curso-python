# Q.50 Jogo da Velha Simples.


# tabuleiro: tab[linha][coluna]
tab = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
quant_jogadas = 0
jogador = 'X'




# imprimir tabuleiro
def imprimir_tab():
    print('\nJOGO DA VELHA')
    print('', tab[0][0], '|', tab[0][1], '|', tab[0][2])
    print('---+---+---')
    print('', tab[1][0], '|', tab[1][1], '|', tab[1][2])
    print('---+---+---')
    print('', tab[2][0], '|', tab[2][1], '|', tab[2][2])




# executar um jogada
def executar_jogada(jogada):
    if jogada == 1 and tab[0][0] == ' ':
        tab[0][0] = jogador
        return True
    elif jogada == 2 and tab[0][1] == ' ':
        tab[0][1] = jogador
        return True
    elif jogada == 3 and tab[0][2] == ' ':
        tab[0][2] = jogador
        return True
    elif jogada == 4 and tab[1][0] == ' ':
        tab[1][0] = jogador
        return True
    elif jogada == 5 and tab[1][1] == ' ':
        tab[1][1] = jogador
        return True
    elif jogada == 6 and tab[1][2] == ' ':
        tab[1][2] = jogador
        return True
    elif jogada == 7 and tab[2][0] == ' ':
        tab[2][0] = jogador
        return True
    elif jogada == 8 and tab[2][1] == ' ':
        tab[2][1] = jogador
        return True
    elif jogada == 9 and tab[2][2] == ' ':
        tab[2][2] = jogador
        return True


    print('\nEscolha uma jogada válida!')
    return False




# verificar se há um ganhador
def verificar_ganhador():
    # verifica as linhas
    if tab[0][0] == tab[0][1] and tab[0][0] == tab[0][2]:
        return tab[0][0]
    elif tab[1][0] == tab[1][1] and tab[1][0] == tab[1][2]:
        return tab[1][0]
    elif tab[2][0] == tab[2][1] and tab[2][0] == tab[2][2]:
        return tab[2][0]
    # verifica as colunas
    elif tab[0][0] == tab[1][0] and tab[0][0] == tab[2][0]:
        return tab[0][0]
    elif tab[0][1] == tab[1][1] and tab[0][1] == tab[2][1]:
        return tab[0][1]
    elif tab[0][2] == tab[1][2] and tab[0][2] == tab[2][2]:
        return tab[0][2]
    # verifica as diagonais
    elif tab[2][0] == tab[1][1] and tab[2][0] == tab[0][2]:
        return tab[2][0]
    elif tab[0][0] == tab[1][1] and tab[0][0] == tab[2][2]:
        return tab[2][2]
    
    return 'VELHA'




# rotina
while quant_jogadas <= 9:
    imprimir_tab()
    jogada = int(input('Escolha uma jogada entre 1 e 9: '))


    jogada_ok = executar_jogada(jogada)
    if jogada_ok == True:
        quant_jogadas += 1


        ganhador = verificar_ganhador()
        if ganhador == 'X' or ganhador == 'O' or quant_jogadas == 9:
            imprimir_tab()
            print('\nGANHADOR:', ganhador)
            break


        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
