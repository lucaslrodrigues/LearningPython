"""
    Introduzir POO com a classe
    Treinar lista dentro da tupla com o endereço completo já dentro de um array (depois preencher este endereco)
"""

class Dicionario:
    def __init__(self):
        self.items = []
        print('\nITEMS = ', self.items)

    def getPerson(self):
        return self.items;

    def push(self, p, e):
        self.items.append({'nome' : f'{p}', 'endereco' : f'{e}'});

    def newPerson(self, *args):
        for i in args:
            p , e = i
            Dicionario.push(self, p, e);