import json

class S:
    def __init__(self, nome):
        self.nome = nome;
    
    def saudacao(self, saudacao):
        def saudar():
            return f'{saudacao} {self.nome}'
        return saudar

pessoa = ['Lucas', 'maria']
for n in pessoa:

    s = S(n);

    saudacao1 = s.saudacao('Bom dia')
    saudacao2 = s.saudacao('Boa noite')

    print(saudacao1())
    print(saudacao2())