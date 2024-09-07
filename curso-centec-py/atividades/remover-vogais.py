# Q.19 Remover vogais de string.


# entrada
texto = input('Digite seu texto: ')


texto_sem_vogais = ''


# processamento
for c in texto:
    if c not in ['a', 'e', 'i', 'o', 'u']:
        texto_sem_vogais += c


# saída
print('Resultado:', texto_sem_vogais)
