

# Q.27 Converter minutos em horas e minutos.


# 1h -> 60min
# 100min -> 1h e 40min
# 210min -> 3h (180min) e 30min


min_entrada = int(input('Digite os minutos: '))


horas = min_entrada // 60
minutos = min_entrada % 60


print(horas, 'horas e', minutos, 'minutos.')
