"""
    Introduzir POO com a classe
    Treinar lista dentro da tupla com o endereço completo já dentro de um array (depois preencher este endereco)
"""

# class dicionario:
#     def __init__(self):
#         self.items = []

#     def push(self):
#         self.items.append({});

#     def newPerson(self, *args):


# pessoa = [];

# pessoa.append({});

# pessoa[0]['nome'] = 'Lucas'

# print(pessoa[0]['nome'])

cadastrados = []

def push(p, e):
    cadastrados.append({'nome' : f'{p}', 'endereco' : f'{e}'});

def addPessoas(*args):
    for p, e in args:
        push(p, e);

addPessoas(('Ana', [{'rua' : 'Vila maria', 'estado' : 'São Paulo', 'numero' : '1056'}]), ('Lucas', 'Jardin Santa Lucrecia'));
print(cadastrados);

for i in cadastrados:
    print('-' * 60)
    for o in i:
        print(o, i[o])