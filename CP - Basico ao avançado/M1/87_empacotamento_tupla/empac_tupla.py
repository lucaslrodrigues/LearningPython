nomes = ['Maria', 'Julinha', 'Guilherme Freitas']

nome1, nome2, nome3 = nomes # desempacotado
# nome1, nome2, nome3 = ['Maria', 'Julinha', 'Guilherme Freitas'] MESMA COISA

print(nome2)

nome1, *resto = ['Maria', 'Julinha', 'Guilherme Freitas']
nome, *_ = ['Maria', 'Julinha', 'Guilherme Freitas'] # _ é uma convenção para variavel para se ignorar

print(nome, _)


# Tupla LISTA IMUTAVEL
nomes = 'Venerdi', 'Sula'
nomes = ('Venerdi', 'Sula')
print(nomes)
nomes = list(nomes) # Convertida para se tornar mutavel
print(nomes)
nomes.append("YANDEH")
print(nomes)
