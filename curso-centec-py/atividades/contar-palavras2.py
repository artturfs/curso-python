

# Q.9 Contar palavras de uma string.

texto = input('Digite seu texto: ')

lista = texto.split()
quant_palavras = len(lista)

print('Quant. de palavras:', quant_palavras)

# 'o rato roeu a roupa do rei de roma'
# ['o', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'roma']