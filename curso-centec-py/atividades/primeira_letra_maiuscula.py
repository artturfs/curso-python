

# Q.38 Primeira letra de cada palavra para maiúscula.


# entrada
texto = input('Digite seu texto: ')


alfabeto = {
    'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F',
    'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L',
    'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R',
    's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X',
    'y':'Y', 'z':'Z'
}


novo_texto = ''


# processamento
lista_palavras = texto.split()


for palavra in lista_palavras:
    primeira_letra = palavra[0]


    letra_maiuscula = alfabeto[primeira_letra]


    nova_palavra = letra_maiuscula + palavra[1:]


    novo_texto += ' ' + nova_palavra


# saída
print('Saída:', novo_texto)
