"""
    SEM SOBRECARGA EM PYTHON!!

    https://pt.stackoverflow.com/questions/317239/como-funciona-o-polimorfismo-de-sobrecarga-em-python

"""

import os
os.system('cls')

class Teste:
    def __init__(self) -> None:
        pass;

    # def soma_sobrecarga (self, x, y):
    #     print(f'x = {x} y = {y} | x + y = {x + y}');
    
    def soma (self, x, y, z = None):
        if z is None:
            print(f'x = {x} y = {y} | x + y = {x + y}');
        else:
            print(f'x = {x} y = {y} z = {z} | x + y + z = {x + y + z}');
    
    # BRINCANDO COM METODOS

    def multiplicarNum(self, num, num2):
        return num * num2;

    def exibirMultiplicacao(self, num, num2):
        res = Teste.multiplicarNum(self, num, num2);
        bar = "-" * 40 + "\n";
        print('%s%d x %d = %d' % (bar, num, num2, res));


teste = Teste();
teste.soma(1, 2); # FALTA DE ARGS E PARAMETROS COM PADRÃO NONE
teste.soma(1, 2, z = 6); # ARGS POSICIONAIS E SIMULAÇÃO DE SOBRECARGA
teste.soma(z = 1, x = 2, y = 6); # ARGS NOMEADOS

teste.exibirMultiplicacao(2, 3);