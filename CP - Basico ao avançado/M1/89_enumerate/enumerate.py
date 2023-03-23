nomes = ['Maria', 'Julinha', 'Guilherme Freitas']
nomes.append('João')

listaEnumerada = enumerate(nomes)
print(next(listaEnumerada)) # Gera uma tupla enumerada

# for i in listaEnumerada:
#     print(i)

for i in enumerate(nomes):
    print(i)

# for i in enumerate(nomes):
#     index, name = i # Desempacotando
#     print(index, name)

for index, name in enumerate(nomes):
    print(index, name)