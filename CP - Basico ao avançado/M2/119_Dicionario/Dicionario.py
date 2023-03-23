# BASIC I
pessoa = {
    'nome' : 'Lucas',
    'nascData' : '09/01/2003',
    'ocupacao' : 'estudante'
}
pessoa['nome'] = 'Jose'
print(pessoa['nome'])
for i in pessoa:
    print(i, pessoa[i])

# BASIC II

pessoa = [{
    'nome' : 'Lucas',
    'nascData' : '09/01/2003',
    'ocupacao' : 'estudante',
    "enderecos" : [{'rua' : 'Domenico Montela'}]
},
{
    'nome' : 'Maria',
    'nascData' : '20/07/2003',
    'ocupacao' : 'estudante',
    "enderecos" : [{'rua' : 'Estr. de Taipas'}]
}]

for i in pessoa:
    print('-' * 60)
    for o in i:
        print(o, i[o])