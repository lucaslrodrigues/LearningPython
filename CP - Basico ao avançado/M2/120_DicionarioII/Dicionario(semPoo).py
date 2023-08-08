# MESMA COISA SÓ QUE SEM POO

cadastrados = []

def push(p, e):
    cadastrados.append({'nome' : f'{p}', 'endereco' : f'{e}'});

def addPessoas(*args):
    for p, e in args:
        push(p, e);

addPessoas(('Ana', [{'rua' : 'Vila maria', 'estado' : 'São Paulo', 'numero' : '1056'}]), ('Lucas', 'Jardin Santa Lucrecia'), ('Maria Helena',[{'rua' : 'Rondonopolis', 'estado' : 'Mato Grosso do sul', 'numero' : '25'}]));
print(cadastrados);

pessoa1 = cadastrados[0]['nome'];
pessoa1 = 'Monica'; # ATRIBUINDO VALORES
print(pessoa1); # ACESSANDO ATRIBUTO

cadastrados[1];
del cadastrados[1]['endereco']; # NÃO É POSSIVEL REFERENCIAR EM VARIAVEL ESTE CAMINHO


for i in cadastrados:
    print('-' * 60)
    for o in i:
        print(o, i[o])
        # print(i, i[o])
print('-' * 60)
