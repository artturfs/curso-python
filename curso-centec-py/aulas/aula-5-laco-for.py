# CONTAGEM
#  +1 +1 +1 +1 +1 +1 +1 +1 +1
# 1  2  3  4  5  6  7  8  9  10
# início: 1
# fim: 10
# passo: 1 (presumido)

# CONTAGEM REGRESSIVA
# 10 até 0
#   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 10  9  8  7  6  5  4  3  2  1  0
# início: 10
# fim: 0
# passo: -1

# CONTAGEM
# início: 1
# fim: 15
# passo: 2
#  +2 +2 +2 +2 +2  +2  +2
# 1  3  5  7  9  11  13  15


# FUNÇÃO RANGE()
# início: 1 (inclusivo)
# fim: 10 (exclusivo)

# 1 - 10
valor = 10
for valor in range(1, 11, 1):
    mult = valor * 5
    print(mult)